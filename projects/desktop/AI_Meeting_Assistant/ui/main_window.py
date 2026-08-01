from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QPushButton,
    QTextEdit,
    QListWidget,
    QLabel,
    QLineEdit,
    QSplitter,
    QVBoxLayout,
    QHBoxLayout,
    QMessageBox,
    QFileDialog,
    QProgressBar
)

from PySide6.QtCore import (
    Qt,
    QThread,
    Signal
)

from PySide6.QtGui import (
    QTextCursor
)

from datetime import datetime
from pathlib import Path

# ==========================
# Audio
# ==========================

from audio.recorder import Recorder

# ==========================
# AI
# ==========================

from ai.whisper_service import (
    transcribe
)

from ai.summary_service import (
    generate_summary
)

from ai.action_service import (
    extract_actions,
    extract_decisions
)

# Speaker Diarization

from ai.speaker_service import (
    diarize
)

from ai.merge_service import (
    merge_segments
)

# ==========================
# Export
# ==========================

from export.word_exporter import (
    export_word
)

from export.pdf_exporter import (
    export_pdf
)

# ==========================
# Database
# ==========================

from database.repository import (
    create_meeting,
    update_meeting,
    get_meeting,
    get_meetings,
    search_meetings,
    save_segment
)

# ==========================
# Worker
# ==========================

from workers.transcription_worker import (
    TranscriptionWorker
)


class MainWindow(QMainWindow):

    def __init__(self):

        super().__init__()

        # ==========================
        # Window
        # ==========================

        self.setWindowTitle(
            "AI Meeting Assistant"
        )

        self.resize(
            1500,
            950
        )

        # ==========================
        # Audio Recorder
        # ==========================

        self.recorder = Recorder()

        # ==========================
        # Worker
        # ==========================

        self.worker = None

        self.transcribe_thread = None

        self.export_thread = None

        # ==========================
        # Meeting State
        # ==========================

        self.current_meeting_id = None

        self.current_transcript = ""

        self.current_summary = ""

        self.current_actions = []

        self.current_decisions = []

        self.is_streaming = False

        # ==========================
        # Build UI
        # ==========================

        self.init_ui()
        self.stop_btn.setEnabled(
            False
        )

        self.disable_export_buttons()
        # ==========================
        # Load History
        # ==========================

        self.load_history()

        self.set_status(
            "Ready"
        )
#--------
#1A
    def init_ui(self):
        
        # ==========================
        # Central Widget
        # ==========================

        central = QWidget()

        self.setCentralWidget(
            central
        )

        root = QVBoxLayout()

        central.setLayout(
            root
        )

        # ==========================
        # Top Toolbar
        # ==========================

        top_layout = QHBoxLayout()

        self.start_btn = QPushButton(
            "🎤 開始錄音"
        )

        self.stop_btn = QPushButton(
            "⏹ 停止錄音"
        )

        self.export_word_btn = QPushButton(
            "📝 匯出 Word"
        )

        self.export_pdf_btn = QPushButton(
            "📄 匯出 PDF"
        )

        self.export_word_btn.setEnabled(
            False
        )

        self.export_pdf_btn.setEnabled(
            False
        )

        top_layout.addWidget(
            self.start_btn
        )

        top_layout.addWidget(
            self.stop_btn
        )

        top_layout.addWidget(
            self.export_word_btn
        )

        top_layout.addWidget(
            self.export_pdf_btn
        )

        top_layout.addStretch()

        # ==========================
        # Search
        # ==========================

        self.search_edit = QLineEdit()

        self.search_edit.setPlaceholderText(
            "搜尋會議..."
        )

        self.search_btn = QPushButton(
            "🔍 搜尋"
        )

        top_layout.addWidget(
            self.search_edit
        )

        top_layout.addWidget(
            self.search_btn
        )

        root.addLayout(
            top_layout
        )

        # ==========================
        # Splitter
        # ==========================

        splitter = QSplitter(
            Qt.Horizontal
        )

        root.addWidget(
            splitter
        )

        # ==========================
        # Left Panel
        # ==========================

        left_widget = QWidget()

        left_layout = QVBoxLayout()

        left_widget.setLayout(
            left_layout
        )

        history_label = QLabel(
            "📚 歷史會議"
        )

        self.history_list = QListWidget()

        left_layout.addWidget(
            history_label
        )

        left_layout.addWidget(
            self.history_list
        )

        splitter.addWidget(
            left_widget
        )

        # ==========================
        # Right Panel
        # ==========================

        right_widget = QWidget()

        right_layout = QVBoxLayout()

        right_widget.setLayout(
            right_layout
        )

        # --------------------------
        # Transcript
        # --------------------------

        transcript_label = QLabel(
            "📜 即時逐字稿"
        )

        self.transcript_text = QTextEdit()

        self.transcript_text.setReadOnly(
            True
        )

        right_layout.addWidget(
            transcript_label
        )

        right_layout.addWidget(
            self.transcript_text
        )

        # --------------------------
        # AI Summary
        # --------------------------

        summary_label = QLabel(
            "🤖 AI 摘要"
        )

        self.summary_text = QTextEdit()

        self.summary_text.setReadOnly(
            True
        )

        right_layout.addWidget(
            summary_label
        )

        right_layout.addWidget(
            self.summary_text
        )

        splitter.addWidget(
            right_widget
        )

        splitter.setSizes(
            [350, 1150]
        )

        # ==========================
        # Progress Bar
        # ==========================

        self.progress = QProgressBar()

        self.progress.setRange(
            0,
            0
        )

        self.progress.hide()

        root.addWidget(
            self.progress
        )

        # ==========================
        # Status Label
        # ==========================

        self.status = QLabel(
            "Ready"
        )

        root.addWidget(
            self.status
        )

        # ==========================
        # Connect Signals
        # ==========================

        self.start_btn.clicked.connect(
            self.start_streaming
        )

        self.stop_btn.clicked.connect(
            self.stop_streaming
        )

        self.export_word_btn.clicked.connect(
            self.export_word_report
        )

        self.export_pdf_btn.clicked.connect(
            self.export_pdf_report
        )

        self.search_btn.clicked.connect(
            self.search_history
        )

        self.history_list.itemClicked.connect(
            self.open_meeting
        )
#--------------------------
#1B
    def set_status(
            self,
            text: str):

        self.status.setText(
            f"Status: {text}"
        )
    def append_text(
            self,
            text: str):

        self.transcript_text.append(
            text
        )

        cursor = (
            self.transcript_text
            .textCursor()
        )

        cursor.movePosition(
            QTextCursor.End
        )

        self.transcript_text.setTextCursor(
            cursor
        )

    def show_error(self, message):
        self.progress.hide()

        QMessageBox.critical(
            self,
            "錯誤",
            str(message)
        )

        self.set_status(
            "Error"
        )

    def update_transcript(
            self,
            text: str):

        if not text.strip():
            return

        self.current_transcript += (
            text + "\n"
        )

        self.append_text(
            text
        )
#--------------------------
#加入即時儲存：
        if self.worker:
        
            self.current_meeting_id = (
                self.worker.meeting_id
            )

        self.enable_export_buttons()
#--------------------------
        self.export_word_btn.setEnabled(
            True
        )

        self.export_pdf_btn.setEnabled(
            True
        )
    def clear_current_session(self):
    
        self.current_transcript = ""

        self.current_summary = ""

        self.current_actions = []

        self.current_decisions = []

        self.current_meeting_id = None

        self.transcript_text.clear()

        self.summary_text.clear()

    def generate_ai_summary(self):
        
        if len(
                self.current_transcript
            ) < 20:

            return

        try:



            self.progress.show()

            self.set_status(
                "AI 摘要生成中..."
            )

            summary = generate_summary(
                self.current_transcript
            )

            self.current_actions = (
                extract_actions(
                    self.current_transcript
                )
            )

            self.current_decisions = (
                extract_decisions(
                    self.current_transcript
                )
            )

            self.current_summary = (
                summary
            )

            self.summary_text.setText(
                summary
            )

            if self.current_meeting_id:

                update_meeting(
                    meeting_id=
                    self.current_meeting_id,

                    summary=summary
                )

            self.set_status(
                "摘要完成"
            )

        except Exception as e:

            self.current_actions = []
            self.current_decisions = []
            QMessageBox.warning(
                self,
                "AI 摘要失敗",
                str(e)
            )

        finally:

            self.progress.hide()

    def enable_export_buttons(self):
        
        self.export_word_btn.setEnabled(
            True
        )

        self.export_pdf_btn.setEnabled(
            True
        )

    def disable_export_buttons(self):
        
        self.export_word_btn.setEnabled(
            False
        )

        self.export_pdf_btn.setEnabled(
            False
        )
#--------------------------
#Part 2

    def start_streaming(self):
        
        if self.worker:

            QMessageBox.information(
                self,
                "提示",
                "錄音已在進行中"
            )

            return

        try:

            self.clear_current_session()

            self.progress.show()

            self.set_status(
                "初始化即時辨識..."
            )

            self.worker = (
                TranscriptionWorker(
                    chunk_seconds=3,
                    meeting_title=
                    f"即時會議 "
                    f"{datetime.now().strftime('%Y-%m-%d %H:%M')}"
                )
            )

            # ==================
            # Signals
            # ==================

            self.worker.new_text.connect(
                self.update_transcript
            )

            self.worker.status_changed.connect(
                self.set_status
            )

            self.worker.error_occurred.connect(
                self.show_error
            )

            # ==================
            # Start
            # ==================
            self.worker.summary_ready.connect(
                self.on_summary_ready
            )

            self.worker.actions_ready.connect(
                self.on_actions_ready
            )

            self.worker.decisions_ready.connect(
                self.on_decisions_ready
            )


            self.worker.start()

            self.is_streaming = True

            self.start_btn.setEnabled(
                False
            )

            self.stop_btn.setEnabled(
                True
            )

            self.disable_export_buttons()

            self.set_status(
                "即時辨識中..."
            )

        except Exception as e:

            QMessageBox.critical(
                self,
                "錯誤",
                str(e)
            )

    def stop_streaming(self):
        
        if not self.worker:

            return

        try:

            self.set_status(
                "停止錄音中..."
            )

            self.worker.stop()

            self.worker.wait()

            self.worker.deleteLater()

            self.worker = None

            self.is_streaming = False

            self.progress.hide()

            self.start_btn.setEnabled(
                True
            )

            self.stop_btn.setEnabled(
                False
            )

            self.enable_export_buttons()

            self.set_status(
                "錄音已停止"
            )

            # ==================
            # AI Summary
            # ==================

            self.generate_ai_summary()

        except Exception as e:

            QMessageBox.critical(
                self,
                "錯誤",
                str(e)
            )
#--------------------------
#避免關閉視窗時背景執行緒未釋放：
#---------------------------
    def closeEvent(
            self,
            event):

        try:

            if self.worker:

                self.worker.stop()

                self.worker.wait()

        except Exception:

            pass

        event.accept()
#--------------------------
#Part 3
#--------------------------
    def load_history(self):
        
        try:

            meetings = get_meetings()

            self.history_list.clear()

            for m in meetings:

                item = (
                    f"{m['id']} | "
                    f"{m['created_at']} | "
                    f"{m['title']}"
                )

                self.history_list.addItem(
                    item
                )

        except Exception as e:

            self.show_error(
                str(e)
            )
    def search_history(self):
        
        try:

            keyword = (
                self.search_edit
                .text()
                .strip()
            )

            if keyword == "":

                self.load_history()

                return

            meetings = search_meetings(
                keyword
            )

            self.history_list.clear()

            for m in meetings:

                item = (
                    f"{m['id']} | "
                    f"{m['created_at']} | "
                    f"{m['title']}"
                )

                self.history_list.addItem(
                    item
                )

        except Exception as e:

            self.show_error(
                str(e)
            )

    def open_meeting(
            self,
            item):

        try:

            meeting_id = int(
                item.text()
                .split("|")[0]
                .strip()
            )

            meeting = get_meeting(
                meeting_id
            )

            if not meeting:
                return

            self.current_meeting_id = (
                meeting_id
            )

            transcript = (
                meeting["transcript"]
                or ""
            )

            summary = (
                meeting["summary"]
                or ""
            )

            self.transcript_text.setText(
                transcript
            )

            self.summary_text.setText(
                summary
            )

            self.current_transcript = (
                transcript
            )

            self.current_summary = (
                summary
            )

            self.enable_export_buttons()

            self.set_status(
                f"載入會議 "
                f"#{meeting_id}"
            )

        except Exception as e:

            self.show_error(
                str(e)
            )

    def export_word_report(self):
        
        try:

            transcript = (
                self.transcript_text
                .toPlainText()
                .strip()
            )

            if not transcript:

                QMessageBox.warning(
                    self,
                    "警告",
                    "沒有可匯出的內容"
                )

                return

            title = (
                f"Meeting_"
                f"{datetime.now().strftime('%Y%m%d_%H%M%S')}"
            )

            file_path, _ = QFileDialog.getSaveFileName(
                self,
                "儲存 Word",
                f"{title}.docx",
                "Word (*.docx)"
            )

            if not file_path:
                return

            export_word(
                output_file=file_path,

                meeting_title=title,

                summary=self.summary_text
                .toPlainText(),

                transcript=transcript,

                actions=self.current_actions,

                decisions=self.current_decisions
            )

            QMessageBox.information(
                self,
                "完成",
                "Word 匯出成功"
            )

        except Exception as e:

            self.show_error(
                str(e)
            )

    def export_pdf_report(self):
        
        try:

            transcript = (
                self.transcript_text
                .toPlainText()
                .strip()
            )

            if not transcript:

                QMessageBox.warning(
                    self,
                    "警告",
                    "沒有可匯出的內容"
                )

                return

            title = (
                f"Meeting_"
                f"{datetime.now().strftime('%Y%m%d_%H%M%S')}"
            )

            file_path, _ = QFileDialog.getSaveFileName(
                self,
                "儲存 PDF",
                f"{title}.pdf",
                "PDF (*.pdf)"
            )

            if not file_path:
                return

            export_pdf(
                output_file=file_path,

                meeting_title=title,

                summary=self.summary_text
                .toPlainText(),

                transcript=transcript,

                actions=self.current_actions,

                decisions=self.current_decisions
            )

            QMessageBox.information(
                self,
                "完成",
                "PDF 匯出成功"
            )

        except Exception as e:

            self.show_error(
                str(e)
            )

    def on_summary_ready(
            self,
            summary):

        self.summary_text.setText(
            summary
        )


    def on_actions_ready(
            self,
            actions):

        self.current_actions = actions


    def on_decisions_ready(
            self,
            decisions):

        self.current_decisions = decisions
