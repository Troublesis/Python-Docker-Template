# https://pypi.org/project/loguru/
import sys

from loguru import logger

from src.utils.config import settings

if settings.get("DEBUG", False) is True:
    DEBUG = True
else:
    DEBUG = False


def my_filter(record):
    return record["level"].name != "DEBUG"


LOG_FORMATS = {
    "normal": "<green>{time:YYYY-MM-DD HH:mm:ss}</green> <level>{level: <8}</level> [{file}:{line}] {message}",
    "error": "<red>{time:YYYY-MM-DD HH:mm:ss}</red> <level>{level: <8}</level> [{file}:{line}] {message}",
}

# Remove the default logger
logger.remove()

logger.configure(
    handlers=[
        {
            "sink": sys.stderr,
            "format": LOG_FORMATS["normal"],
            "level": "DEBUG" if DEBUG else "INFO",
            "filter": None if DEBUG else my_filter,
        },
        {
            "sink": "logs/access.log",
            "format": LOG_FORMATS["normal"],
            "rotation": "100 MB",
            "retention": "7 days",
        },
        {
            "sink": "logs/error.log",
            "format": LOG_FORMATS["error"],
            "level": "ERROR",
            "rotation": "100 MB",
        },
    ]
)

if __name__ == "__main__":
    logger.info("Hello World!")
    logger.debug("This is a debug message")
    logger.warning(f"Warning: Something wrong")
    logger.error("Something went wrong.")
    logger.critical("Critical error!")
