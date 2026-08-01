from dataclasses import dataclass
from typing import Optional


@dataclass
class Meeting:
    """
    會議主表
    """

    id: Optional[int] = None
    title: str = ""
    transcript: str = ""
    summary: str = ""
    created_at: str = ""


@dataclass
class TranscriptSegment:
    """
    逐字稿段落
    """

    id: Optional[int] = None
    meeting_id: Optional[int] = None

    speaker: str = "Speaker 1"

    start_time: float = 0.0
    end_time: float = 0.0

    content: str = ""


@dataclass
class ActionItem:
    """
    AI待辦事項
    """

    id: Optional[int] = None
    meeting_id: Optional[int] = None

    owner: str = ""
    task: str = ""
    deadline: str = ""
    status: str = "Open"


@dataclass
class Decision:
    """
    決策事項
    """

    id: Optional[int] = None
    meeting_id: Optional[int] = None

    decision: str = ""
    created_at: str = ""


@dataclass
class Speaker:
    """
    說話人
    """

    id: Optional[int] = None
    meeting_id: Optional[int] = None

    name: str = ""
    duration: float = 0.0
    percentage: float = 0.0