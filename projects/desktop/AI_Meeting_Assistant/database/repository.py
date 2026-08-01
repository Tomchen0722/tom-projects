import sqlite3
from pathlib import Path
from datetime import datetime

DB_PATH = Path(__file__).parent / "meeting.db"


def get_connection():
    """
    建立 SQLite 連線
    """

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    return conn


def init_db():
    """
    初始化資料庫
    """

    conn = get_connection()
    cur = conn.cursor()

    # 會議主表
    cur.execute("""
    CREATE TABLE IF NOT EXISTS meetings(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        transcript TEXT,
        summary TEXT,
        created_at TEXT
    )
    """)

    # 逐字稿段落
    cur.execute("""
    CREATE TABLE IF NOT EXISTS transcript_segments(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        meeting_id INTEGER,
        speaker TEXT,
        start_time REAL,
        end_time REAL,
        content TEXT,

        FOREIGN KEY(meeting_id)
        REFERENCES meetings(id)
        ON DELETE CASCADE
    )
    """)

    # 待辦事項
    cur.execute("""
    CREATE TABLE IF NOT EXISTS action_items(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        meeting_id INTEGER,
        owner TEXT,
        task TEXT,
        deadline TEXT,
        status TEXT,

        FOREIGN KEY(meeting_id)
        REFERENCES meetings(id)
        ON DELETE CASCADE
    )
    """)

    # 決策事項
    cur.execute("""
    CREATE TABLE IF NOT EXISTS decisions(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        meeting_id INTEGER,
        decision TEXT,
        created_at TEXT,

        FOREIGN KEY(meeting_id)
        REFERENCES meetings(id)
        ON DELETE CASCADE
    )
    """)

    conn.commit()
    conn.close()


# ==========================
# Meeting CRUD
# ==========================

def create_meeting(
        title: str,
        transcript: str = "",
        summary: str = "") -> int:

    conn = get_connection()
    cur = conn.cursor()

    created_at = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    cur.execute("""
    INSERT INTO meetings(
        title,
        transcript,
        summary,
        created_at
    )
    VALUES (?,?,?,?)
    """, (
        title,
        transcript,
        summary,
        created_at
    ))

    conn.commit()

    meeting_id = cur.lastrowid

    conn.close()

    return meeting_id


def update_meeting(
        meeting_id: int,
        transcript: str = None,
        summary: str = None):

    conn = get_connection()
    cur = conn.cursor()

    if transcript is not None:
        cur.execute("""
        UPDATE meetings
        SET transcript=?
        WHERE id=?
        """, (
            transcript,
            meeting_id
        ))

    if summary is not None:
        cur.execute("""
        UPDATE meetings
        SET summary=?
        WHERE id=?
        """, (
            summary,
            meeting_id
        ))

    conn.commit()
    conn.close()


def get_meeting(meeting_id: int):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    SELECT *
    FROM meetings
    WHERE id=?
    """, (meeting_id,))

    row = cur.fetchone()

    conn.close()

    return row


def get_meetings():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    SELECT *
    FROM meetings
    ORDER BY id DESC
    """)

    rows = cur.fetchall()

    conn.close()

    return rows


def delete_meeting(meeting_id: int):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    DELETE FROM meetings
    WHERE id=?
    """, (meeting_id,))

    conn.commit()
    conn.close()


# ==========================
# Transcript Segment
# ==========================

def save_segment(
        meeting_id: int,
        speaker: str,
        start_time: float,
        end_time: float,
        content: str):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    INSERT INTO transcript_segments(
        meeting_id,
        speaker,
        start_time,
        end_time,
        content
    )
    VALUES (?,?,?,?,?)
    """, (
        meeting_id,
        speaker,
        start_time,
        end_time,
        content
    ))

    conn.commit()
    conn.close()


def get_segments(meeting_id: int):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    SELECT *
    FROM transcript_segments
    WHERE meeting_id=?
    ORDER BY start_time
    """, (meeting_id,))

    rows = cur.fetchall()

    conn.close()

    return rows


# ==========================
# Action Items
# ==========================

def save_action(
        meeting_id: int,
        owner: str,
        task: str,
        deadline: str = "",
        status: str = "Open"):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    INSERT INTO action_items(
        meeting_id,
        owner,
        task,
        deadline,
        status
    )
    VALUES (?,?,?,?,?)
    """, (
        meeting_id,
        owner,
        task,
        deadline,
        status
    ))

    conn.commit()
    conn.close()


def get_actions(meeting_id: int):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    SELECT *
    FROM action_items
    WHERE meeting_id=?
    """, (meeting_id,))

    rows = cur.fetchall()

    conn.close()

    return rows


# ==========================
# Decisions
# ==========================

def save_decision(
        meeting_id: int,
        decision: str):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    INSERT INTO decisions(
        meeting_id,
        decision,
        created_at
    )
    VALUES (?,?,?)
    """, (
        meeting_id,
        decision,
        datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )
    ))

    conn.commit()
    conn.close()


def get_decisions(meeting_id: int):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    SELECT *
    FROM decisions
    WHERE meeting_id=?
    """, (meeting_id,))

    rows = cur.fetchall()

    conn.close()

    return rows


# ==========================
# Search
# ==========================

def search_meetings(keyword: str):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    SELECT *
    FROM meetings
    WHERE title LIKE ?
       OR transcript LIKE ?
    ORDER BY id DESC
    """, (
        f"%{keyword}%",
        f"%{keyword}%"
    ))

    rows = cur.fetchall()

    conn.close()

    return rows