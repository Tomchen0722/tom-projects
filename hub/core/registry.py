# -*- coding: utf-8 -*-
"""讀取 projects.json 登記檔。

要新增專案時只需要改 projects.json，不必動任何程式碼。
每次請求都重新讀檔，所以編輯完重整瀏覽器就會看到新卡片，不用重啟 Hub。
"""
from __future__ import annotations

import json
from pathlib import Path


class Registry:
    def __init__(self, config_path: Path):
        self.config_path = config_path
        self._cache: dict | None = None
        self._mtime: float = 0.0

    def load(self) -> dict:
        """讀取設定；檔案有變動才重新解析。"""
        mtime = self.config_path.stat().st_mtime
        if self._cache is None or mtime != self._mtime:
            with open(self.config_path, encoding="utf-8") as f:
                self._cache = json.load(f)
            self._mtime = mtime
        return self._cache

    @property
    def hub(self) -> dict:
        return self.load().get("hub", {})

    @property
    def categories(self) -> list[dict]:
        return self.load().get("categories", [])

    @property
    def apps(self) -> list[dict]:
        return self.load().get("apps", [])

    def get(self, app_id: str) -> dict | None:
        for app in self.apps:
            if app["id"] == app_id:
                return app
        return None

    def tree(self) -> list[dict]:
        """組成「大類 → 子類 → 專案」的樹狀結構給前端渲染。"""
        apps = self.apps
        result = []
        for cat in self.categories:
            subs = []
            for sub in cat.get("sub", []):
                items = [
                    a for a in apps
                    if a.get("category") == cat["id"] and a.get("sub") == sub["id"]
                ]
                if items:
                    subs.append({**sub, "apps": items})
            count = sum(len(s["apps"]) for s in subs)
            result.append({**cat, "sub": subs, "count": count})
        return result
