import sys
import traceback
from pathlib import Path
# PySide6.QtWidgets
from PySide6.QtWidgets import (
    QApplication,
    QMessageBox
)

from database.repository import init_db
from ui.main_window import MainWindow


def setup_directories():
    """
    建立必要資料夾
    """

    folders = [
        "reports",
        "assets",
        "database"
    ]

    for folder in folders:

        Path(folder).mkdir(
            exist_ok=True
        )


def exception_hook(
        exc_type,
        exc_value,
        exc_tb):
    """
    全域例外處理
    """

    error = "".join(
        traceback.format_exception(
            exc_type,
            exc_value,
            exc_tb
        )
    )

    print(error)

    QMessageBox.critical(
        None,
        "系統錯誤",
        error
    )


def main():

    # 建立必要資料夾
    setup_directories()

    # 初始化 SQLite
    init_db()

    # 建立 Qt App
    app = QApplication(
        sys.argv
    )

    app.setApplicationName(
        "AI Meeting Assistant"
    )

    app.setOrganizationName(
        "Tom AI Studio"
    )

    # 設定全域錯誤攔截
    sys.excepthook = (
        exception_hook
    )

    # 建立主視窗
    window = MainWindow()

    window.show()

    sys.exit(
        app.exec()
    )


if __name__ == "__main__":

    main()