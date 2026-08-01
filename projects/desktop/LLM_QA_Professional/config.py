from pathlib import Path
import os
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parent

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
OPENAI_MODEL = "gpt-4o-mini"

ROOT = Path(__file__).resolve().parent

load_dotenv()

# API
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

# Folders
APP_DIR = ROOT
DATA_DIR = ROOT / "data"
LOG_DIR = ROOT / "logs"
UPLOAD_DIR = ROOT / "uploads"
VECTOR_DIR = ROOT / "vector"

for p in [DATA_DIR, LOG_DIR, UPLOAD_DIR, VECTOR_DIR]:
    p.mkdir(parents=True, exist_ok=True)

# App
APP_NAME = "LLM Professional Edition V2"
VERSION = "2.0.0-alpha"
WINDOW_SIZE = "1200x800"