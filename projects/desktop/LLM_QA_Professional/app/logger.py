from loguru import logger
from config import LOG_DIR

LOG_FILE = LOG_DIR / "app.log"

def setup_logger():
    logger.add(LOG_FILE, rotation="10 MB")
    return logger