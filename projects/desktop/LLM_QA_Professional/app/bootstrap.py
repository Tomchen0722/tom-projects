from app.logger import setup_logger
from config import APP_NAME, VERSION

def bootstrap():
    logger = setup_logger()

    logger.info(f"Starting {APP_NAME}")
    logger.info(f"Version: {VERSION}")

    return {
        "app_name": APP_NAME,
        "version": VERSION,
        "status": "ok"
    }