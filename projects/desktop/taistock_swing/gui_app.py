"""台股波段回測｜圖形介面（雙擊可執行）。

可自行輸入股票代碼、日期區間、持有檔數、再平衡天數、基準、訊號類型與回測模式，
按「執行回測」後在下方顯示進度與評估報告。回測在背景執行緒進行，介面不卡住。

啟動若發生錯誤，會寫入與程式同目錄的 error.log 並跳出訊息框（避免 --windowed
打包後靜默失敗看不到原因）。以 PyInstaller 打包成單一 exe：見 build_exe.bat。
"""
from __future__ import annotations

import io
import os
import queue
import sys
import threading
import traceback
from contextlib import redirect_stdout
from pathlib import Path

import tkinter as tk
from tkinter import messagebox, scrolledtext, ttk


def _base_dir() -> Path:
    """程式所在目錄（onefile exe 為 exe 所在處，否則為原始碼所在處）。"""
    if getattr(sys, "frozen", False):
        return Path(sys.executable).resolve().parent
    return Path(__file__).resolve().parent


def _log_fatal(msg: str) -> None:
    """把致命錯誤寫入 error.log 並嘗試跳出訊息框。"""
    try:
        (_base_dir() / "error.log").write_text(msg, encoding="utf-8")
    except Exception:
        pass
    try:
        r = tk.Tk()
        r.withdraw()
        messagebox.showerror("啟動錯誤（請把 error.log 傳給我）", msg[-2000:])
        r.destroy()
    except Exception:
        pass


# 讓 script 模式能匯入 src；exe 模式由 PyInstaller 打包（--paths src + hidden-import）
sys.path.insert(0, str(_base_dir() / "src"))

# 風險匯入獨立攔截：若這裡失敗（多半是打包漏了模組），把原因寫出來而非靜默死亡
try:
    from backtest_runner import SIGNAL_CHOICES, run_backtest_pipeline
    from data_source import DataSource
except Exception:
    _log_fatal("模組匯入失敗（可能是打包漏了套件）：\n\n" + traceback.format_exc())
    sys.exit(1)

DEFAULT_UNIVERSE = (
    "2330 2317 2454 2308 2382 2412 2881 2882 2886 2891 "
    "1301 1303 2002 2603 2379 2357 2409 3008 2303 3711 "
    "2884 2885 2887 2890 2892 5880 2880 2883 2609 2615 "
    "1216 1101 1102 2207 2301 2327 2345 2377 2395 3034 "
    "3231 2408 3037 4938 2912 2105 2474 3045 4904 6505"
)


class _QueueWriter(io.TextIOBase):
    """把寫入導向佇列的類檔案物件，供 stdout 重導向到 GUI。"""

    def __init__(self, q: "queue.Queue[str]") -> None:
        self._q = q

    def write(self, text: str) -> int:
        if text:
            self._q.put(text)
        return len(text)


class BacktestApp:
    """回測圖形介面主體。"""

    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("台股波段回測")
        self.root.geometry("900x700")
        self._queue: "queue.Queue[str]" = queue.Queue()
        self._running = False
        self._build_inputs()
        self._build_output()
        self.root.after(100, self._drain_queue)

    def _build_inputs(self) -> None:
        frm = ttk.Frame(self.root, padding=10)
        frm.pack(fill="x")

        ttk.Label(frm, text="FinMind Token（留空則讀環境變數）：").grid(row=0, column=0, sticky="w")
        self.token_var = tk.StringVar()
        ttk.Entry(frm, textvariable=self.token_var, show="*", width=50).grid(
            row=0, column=1, columnspan=3, sticky="we", pady=2)

        ttk.Label(frm, text="股票代碼（空白或逗號分隔）：").grid(row=1, column=0, sticky="nw", pady=2)
        self.universe_text = tk.Text(frm, height=4, width=60, wrap="word")
        self.universe_text.insert("1.0", DEFAULT_UNIVERSE)
        self.universe_text.grid(row=1, column=1, columnspan=3, sticky="we", pady=2)

        ttk.Label(frm, text="起始日：").grid(row=2, column=0, sticky="w", pady=2)
        self.start_var = tk.StringVar(value="2022-01-01")
        ttk.Entry(frm, textvariable=self.start_var, width=14).grid(row=2, column=1, sticky="w")
        ttk.Label(frm, text="結束日：").grid(row=2, column=2, sticky="e", pady=2)
        self.end_var = tk.StringVar(value="2024-12-31")
        ttk.Entry(frm, textvariable=self.end_var, width=14).grid(row=2, column=3, sticky="w")

        ttk.Label(frm, text="基準代碼：").grid(row=3, column=0, sticky="w", pady=2)
        self.benchmark_var = tk.StringVar(value="0050")
        ttk.Entry(frm, textvariable=self.benchmark_var, width=14).grid(row=3, column=1, sticky="w")

        ttk.Label(frm, text="持有檔數：").grid(row=4, column=0, sticky="w", pady=2)
        self.topk_var = tk.IntVar(value=5)
        ttk.Spinbox(frm, from_=1, to=50, textvariable=self.topk_var, width=6).grid(row=4, column=1, sticky="w")
        ttk.Label(frm, text="再平衡天數：").grid(row=4, column=2, sticky="e", pady=2)
        self.rebalance_var = tk.IntVar(value=5)
        ttk.Spinbox(frm, from_=1, to=60, textvariable=self.rebalance_var, width=6).grid(row=4, column=3, sticky="w")

        ttk.Label(frm, text="訊號類型：").grid(row=5, column=0, sticky="w", pady=2)
        self.signal_var = tk.StringVar(value=SIGNAL_CHOICES[0])
        ttk.OptionMenu(frm, self.signal_var, SIGNAL_CHOICES[0], *SIGNAL_CHOICES).grid(
            row=5, column=1, columnspan=2, sticky="w")

        # 原本這裡有「回測模式」下拉選單，但 backtest_runner 沒有定義 MODE_CHOICES，
        # 而且 run_backtest_pipeline 也不讀 params["mode"]，選了不會影響任何結果。
        # 移除選單讓程式能正常啟動；日後真的要做多模式回測時，
        # 要先在 backtest_runner 定義選項並讓 pipeline 實際使用它。

        self.run_btn = ttk.Button(frm, text="執行回測", command=self._on_run)
        self.run_btn.grid(row=6, column=0, columnspan=4, pady=8)
        frm.columnconfigure(1, weight=1)
        frm.columnconfigure(3, weight=1)

    def _build_output(self) -> None:
        self.output = scrolledtext.ScrolledText(self.root, wrap="word", font=("Consolas", 10))
        self.output.pack(fill="both", expand=True, padx=10, pady=(0, 10))
        self.output.configure(state="disabled")

    def _append(self, text: str) -> None:
        self.output.configure(state="normal")
        self.output.insert("end", text)
        self.output.see("end")
        self.output.configure(state="disabled")

    def _drain_queue(self) -> None:
        try:
            while True:
                self._append(self._queue.get_nowait())
        except queue.Empty:
            pass
        self.root.after(100, self._drain_queue)

    def _on_run(self) -> None:
        if self._running:
            return
        self._running = True
        self.run_btn.configure(state="disabled", text="執行中…")
        self.output.configure(state="normal")
        self.output.delete("1.0", "end")
        self.output.configure(state="disabled")

        raw = self.universe_text.get("1.0", "end").replace(",", " ")
        params = {
            "universe": raw.split(),
            "start": self.start_var.get().strip(),
            "end": self.end_var.get().strip(),
            "benchmark_id": self.benchmark_var.get().strip(),
            "top_k": self.topk_var.get(),
            "rebalance_days": self.rebalance_var.get(),
            "signal_choice": self.signal_var.get(),
        }
        token = self.token_var.get().strip() or None
        threading.Thread(target=self._worker, args=(params, token), daemon=True).start()

    def _worker(self, params: dict, token: str | None) -> None:
        writer = _QueueWriter(self._queue)
        try:
            with redirect_stdout(writer):
                ds = DataSource(token=token)
                result = run_backtest_pipeline(params, ds, log=lambda m: self._queue.put(m + "\n"))
                self._queue.put("\n" + str(result["report"]) + "\n")
        except Exception as exc:  # noqa: BLE001
            self._queue.put(f"\n[錯誤] {exc}\n")
            if not (token or os.environ.get("FINMIND_TOKEN")):
                self._queue.put("提示：請在上方輸入 FinMind Token（免費帳號即可）。\n")
        finally:
            self.root.after(0, self._done)

    def _done(self) -> None:
        self._running = False
        self.run_btn.configure(state="normal", text="執行回測")


def main() -> None:
    """啟動圖形介面（含啟動錯誤攔截）。"""
    try:
        root = tk.Tk()
        BacktestApp(root)
        root.mainloop()
    except Exception:
        _log_fatal("啟動時發生錯誤：\n\n" + traceback.format_exc())
        sys.exit(1)


if __name__ == "__main__":
    main()
