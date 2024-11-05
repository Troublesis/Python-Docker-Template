from src.utils.config import settings
from src.utils.logger import logger


def main():
    pass
    logger.info("Hello World!")
    logger.debug("This is a debug message")
    logger.warning("Warning: Something %s", "might")
    logger.error("Something went wrong.")
    logger.critical("Critical error!")
    print(settings.test)


if __name__ == "__main__":
    main()
