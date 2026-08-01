from PySide6.QtCore import (
    QThread,
    Signal
)

from pathlib import Path
import traceback

from audio.stream import AudioStream

from ai.whisper_service import transcribe
from ai.speaker_service import diarize
from ai.merge_service import merge_segments

from ai.summary_service import (
    generate_summary
)

from ai.action_service import (
    extract_actions,
    extract_decisions
)

from database.repository import (
    create_meeting,
    save_segment,
    update_meeting
)


class TranscriptionWorker(QThread):

    # UI 更新
    new_text = Signal(str)

    # 狀態
    status_changed = Signal(str)

    # 錯誤
    error_occurred = Signal(str)

    # AI 摘要完成
    summary_ready = Signal(str)

    # Action Items
    actions_ready = Signal(list)

    # Decision Log
    decisions_ready = Signal(list)

    def __init__(
            self,
            meeting_title="即時會議",
            chunk_seconds=5):

        super().__init__()

        self.running = False

        self.last_text = ""

        self.full_transcript = ""

        self.chunk_seconds = (
            chunk_seconds
        )

        # 建立會議
        self.meeting_id = (
            create_meeting(
                title=meeting_title
            )
        )

        # Audio Stream
        self.stream = AudioStream(
            sample_rate=16000,
            channels=1,
            chunk_seconds=
            chunk_seconds
        )

    def run(self):

        try:

            self.running = True

            self.stream.start()

            self.status_changed.emit(
                "即時辨識中..."
            )

            while self.running:

                wav = (
                    self.stream
                    .get_chunk()
                )

                if not wav:
                    continue

                try:

                    # ==================
                    # Whisper
                    # ==================

                    whisper_result = (
                        transcribe(
                            wav
                        )
                    )

                    segments = (
                        whisper_result[
                            "segments"
                        ]
                    )

                    # ==================
                    # Speaker
                    # ==================

                    try:

                        speakers = (
                            diarize(
                                wav
                            )
                        )

                        merged = (
                            merge_segments(
                                segments,
                                speakers
                            )
                        )

                    except Exception:

                        merged = []

                        for seg in segments:

                            merged.append(
                                {
                                    "speaker":
                                    "Speaker 1",

                                    "start":
                                    seg["start"],

                                    "end":
                                    seg["end"],

                                    "text":
                                    seg["text"]
                                }
                            )

                    ui_text = ""

                    for seg in merged:

                        line = (
                            f"[{seg['speaker']}] "
                            f"{seg['text']}"
                        )

                        ui_text += (
                            line + "\n"
                        )

                        save_segment(
                            meeting_id=
                            self.meeting_id,

                            speaker=
                            seg["speaker"],

                            start_time=
                            seg["start"],

                            end_time=
                            seg["end"],

                            content=
                            seg["text"]
                        )

                    # 避免重複
                    if (
                        ui_text.strip()
                        and
                        ui_text !=
                        self.last_text
                    ):

                        self.last_text = (
                            ui_text
                        )

                        self.full_transcript += (
                            ui_text
                            + "\n"
                        )

                        update_meeting(
                            meeting_id=
                            self.meeting_id,

                            transcript=
                            self.full_transcript
                        )

                        self.new_text.emit(
                            ui_text
                        )

                finally:

                    try:
                        self.stream.cleanup_temp_file(
                            wav
                        )
                    except:
                        pass

            self.stream.stop()

            self.status_changed.emit(
                "產生 AI 摘要..."
            )

            self.generate_ai()

            self.status_changed.emit(
                "完成"
            )

        except Exception as e:

            traceback.print_exc()

            self.error_occurred.emit(
                str(e)
            )

    def generate_ai(self):

        if len(
                self.full_transcript
            ) < 20:

            return

        try:

            # GPT 摘要
            summary = (
                generate_summary(
                    self.full_transcript
                )
            )

            update_meeting(
                meeting_id=
                self.meeting_id,

                summary=
                summary
            )

            self.summary_ready.emit(
                summary
            )

        except Exception as e:

            print(
                "Summary Error:",
                e
            )

        try:

            actions = (
                extract_actions(
                    self.full_transcript
                )
            )

            self.actions_ready.emit(
                actions
            )

        except Exception as e:

            print(
                "Action Error:",
                e
            )

        try:

            decisions = (
                extract_decisions(
                    self.full_transcript
                )
            )

            self.decisions_ready.emit(
                decisions
            )

        except Exception as e:

            print(
                "Decision Error:",
                e
            )

    def stop(self):

        self.running = False

        try:

            self.stream.stop()

        except Exception:
            pass
        