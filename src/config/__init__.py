# https://dynaconf.readthedocs.io/en/docs_223/guides/accessing_values.html
# https://www.dynaconf.com/validation/
import sys

from dynaconf import Dynaconf, Validator
from loguru import logger

settings = Dynaconf(
    envvar_prefix=False,
    load_dotenv=True,
    root_path="/volume1/System/CloudDoc/code/docker/telegram-bot/src/utils",
    settings_files=["settings.toml"],
    environments=True,
    validators=[Validator("DEBUG", must_exist=True, is_type_of=bool)],
)

# https://pypi.org/project/loguru/


DEBUG = settings.get("DEBUG", False)


def my_filter(record):
    return record["level"].name != "DEBUG"


LOG_FORMATS = {
    "normal": "<green>{time:YYYY-MM-DD HH:mm:ss}</green> <level>{level: <8}</level> [{file}:{line}] {message}",
    "warn": "<yellow>{time:YYYY-MM-DD HH:mm:ss}</yellow> <level>{level: <8}</level> [{file}:{line}] {message}",
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
            "sink": "logs/warning.log",
            "format": LOG_FORMATS["warn"],
            "level": "WARNING",
            "rotation": "100 MB",
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

    # print(settings.from_env("exoticaz").get("headers"))


# `envvar_prefix` = export envvars with `export DYNACONF_FOO=bar`.
# `settings_files` = Load these files in the order.

# Example of accessing values with nice comments
# Get a dictionary from settings
# settings["a_dict"]

# Convert a string to boolean from settings
# settings.as_bool("a_boolean")

# Convert a JSON string to a dictionary
# a_dict = '{"key": "value"}'
# settings.as_json("a_dict")

# Get a JSON
# header = '@json {"accept": "text/html"}'
# settings.from_env("html").get("header")

# Get a value from settings, use default if not exists
# settings.get("number", fresh=True)
# settings.from_env("qbit").get("icon", fresh=True)

# Load settings from environment, then get number
# settings.from_env("production").number

# Get a nested value from a dictionary, use default if not exists
# settings.mysql.auth.get("user", "default_user")
