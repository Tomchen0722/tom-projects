# -*- coding: utf-8 -*-
"""把桌面程式的視窗帶到最前面（Windows 專用）。

Hub 是背景服務，由它啟動的 GUI 視窗不會自動取得焦點——Windows 的前景鎖定
機制只會讓工作列圖示閃爍。使用者按了「啟動」卻看不到視窗，體驗很差，
所以這裡主動找出視窗並嘗試前景化。

要注意的兩件事：
1. 虛擬環境的 pythonw.exe 常常只是啟動代理，真正的視窗屬於它的子程序，
   所以要往下遍歷整棵程序樹。
2. SetForegroundWindow 可能被系統拒絕。失敗時退而求其次讓視窗閃爍，
   至少使用者知道要去工作列找。
"""
from __future__ import annotations

import ctypes
import time
from ctypes import wintypes

try:
    user32 = ctypes.WinDLL("user32", use_last_error=True)
    kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
    _AVAILABLE = True
except Exception:  # noqa: BLE001 - 非 Windows 環境就整個停用
    _AVAILABLE = False

SW_RESTORE = 9
SW_SHOW = 5


TH32CS_SNAPPROCESS = 0x00000002


class PROCESSENTRY32(ctypes.Structure):
    _fields_ = [
        ("dwSize", wintypes.DWORD),
        ("cntUsage", wintypes.DWORD),
        ("th32ProcessID", wintypes.DWORD),
        ("th32DefaultHeapID", ctypes.POINTER(ctypes.c_ulong)),
        ("th32ModuleID", wintypes.DWORD),
        ("cntThreads", wintypes.DWORD),
        ("th32ParentProcessID", wintypes.DWORD),
        ("pcPriClassBase", ctypes.c_long),
        ("dwFlags", wintypes.DWORD),
        ("szExeFile", ctypes.c_char * 260),
    ]


def _process_pairs() -> list[tuple[int, int]]:
    """列出系統上所有的 (父程序, 子程序) 配對。

    用 toolhelp 快照而不是 wmic——後者在較新的 Windows 已被移除。
    """
    snapshot = kernel32.CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, 0)
    if snapshot == -1:
        return []

    pairs: list[tuple[int, int]] = []
    entry = PROCESSENTRY32()
    entry.dwSize = ctypes.sizeof(PROCESSENTRY32)
    try:
        if kernel32.Process32First(snapshot, ctypes.byref(entry)):
            while True:
                pairs.append((entry.th32ParentProcessID, entry.th32ProcessID))
                if not kernel32.Process32Next(snapshot, ctypes.byref(entry)):
                    break
    finally:
        kernel32.CloseHandle(snapshot)
    return pairs


def _child_pids(parent_pid: int) -> set[int]:
    """取得整棵程序樹的 PID（含自己）。

    虛擬環境的 pythonw.exe 常常只是啟動代理，真正開視窗的是它的子程序，
    所以必須往下找完整棵樹。
    """
    if not _AVAILABLE:
        return {parent_pid}

    pids = {parent_pid}
    try:
        pairs = _process_pairs()
    except Exception:  # noqa: BLE001
        return pids

    # 反覆展開，直到沒有新的子程序加入
    for _ in range(6):
        before = len(pids)
        for parent, pid in pairs:
            if parent in pids:
                pids.add(pid)
        if len(pids) == before:
            break
    return pids


def find_windows(pids: set[int]) -> list[int]:
    """列出這些程序擁有的可見頂層視窗控制代碼。"""
    if not _AVAILABLE:
        return []

    handles: list[int] = []

    @ctypes.WINFUNCTYPE(wintypes.BOOL, wintypes.HWND, wintypes.LPARAM)
    def callback(hwnd, _lparam):
        if not user32.IsWindowVisible(hwnd):
            return True
        pid = wintypes.DWORD()
        user32.GetWindowThreadProcessId(hwnd, ctypes.byref(pid))
        if pid.value in pids:
            length = user32.GetWindowTextLengthW(hwnd)
            if length > 0:          # 沒有標題的多半是隱藏的工具視窗
                handles.append(hwnd)
        return True

    try:
        user32.EnumWindows(callback, 0)
    except Exception:  # noqa: BLE001
        return []
    return handles


def bring_to_front(pid: int, timeout: float = 20.0) -> bool:
    """等視窗出現後把它帶到最前面。回傳是否找到視窗。

    找不到視窗不代表啟動失敗——有些程式初始化很久，或者刻意常駐在系統匣。
    """
    if not _AVAILABLE:
        return False

    deadline = time.time() + timeout
    handles: list[int] = []
    while time.time() < deadline:
        handles = find_windows(_child_pids(pid))
        if handles:
            break
        time.sleep(0.8)

    if not handles:
        return False

    hwnd = handles[0]
    try:
        user32.ShowWindow(hwnd, SW_RESTORE)
        user32.SetWindowPos(hwnd, -1, 0, 0, 0, 0, 0x0001 | 0x0002)  # HWND_TOPMOST
        user32.SetWindowPos(hwnd, -2, 0, 0, 0, 0, 0x0001 | 0x0002)  # HWND_NOTOPMOST
        if not user32.SetForegroundWindow(hwnd):
            # 系統拒絕搶焦點時，退而求其次讓工作列圖示閃爍
            user32.FlashWindow(hwnd, True)
    except Exception:  # noqa: BLE001
        return True   # 視窗確實存在，只是沒能前景化

    return True


def window_title(pid: int) -> str:
    """取得該程序樹第一個可見視窗的標題，用來回報給使用者。"""
    if not _AVAILABLE:
        return ""
    handles = find_windows(_child_pids(pid))
    if not handles:
        return ""
    length = user32.GetWindowTextLengthW(handles[0])
    buf = ctypes.create_unicode_buffer(length + 1)
    user32.GetWindowTextW(handles[0], buf, length + 1)
    return buf.value
