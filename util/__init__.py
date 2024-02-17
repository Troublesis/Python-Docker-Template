import configparser
import logging
import logging.handlers
import sys
from logging.handlers import RotatingFileHandler


def setup_logger(
    log_name, console_level=logging.INFO, file_level=logging.DEBUG, log_dir="log"
):
    """
    Set up a logger with specified log levels for console and file.

    :param log_name: Name of the logger.
    :param console_level: Logging level for the console handler. Default is INFO.
    :param file_level: Logging level for the file handler. Default is DEBUG.
    :param log_dir: Directory for log files. Default is 'log'.
    :return: Configured logger.
    """

    log = logging.getLogger(log_name)
    log.setLevel(
        min(console_level, file_level)
    )  # Set to the lowest level of both handlers

    # File handler setup
    file_handler = RotatingFileHandler(
        f"{log_dir}/{log_name}.log", maxBytes=5 * 1024 * 1024, backupCount=5
    )
    file_handler.setLevel(file_level)

    # Console handler setup
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(console_level)

    # Log format
    formatter = logging.Formatter(
        "[%(levelname).3s][%(asctime)s][%(filename)s:%(lineno)d] - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Adding handlers to the logger
    log.addHandler(file_handler)
    log.addHandler(console_handler)

    return log


log = setup_logger("log")


def config(category, key, filename="config.ini"):
    """
    Reads and returns a specific configuration value from a configuration file.

    This function attempts to read a value based on a given category (section) and key from a specified
    configuration file. It includes error handling to gracefully manage scenarios where the file might not exist,
    the specified category (section) is not found, or the key is not present in the category.

    Parameters:
    - filename (str): The name of the configuration file. Defaults to 'config.ini'.
    - category (str): The section in the configuration file from which to retrieve the value.
    - key (str): The key within the specified section whose value is to be retrieved.

    Returns:
    - str: The value associated with the specified key within the given category.

    Raises:
    - FileNotFoundError: If the specified configuration file does not exist.
    - KeyError: If the specified category (section) or key is not found in the configuration file.
    """
    config = configparser.ConfigParser()

    # Ensure the configuration file exists
    try:
        config.read(filename)
        # Check if the file was successfully parsed and contains the category
        if category in config:
            # Attempt to retrieve the value using the specified key
            try:
                value = config[category][key]
                return value
            except KeyError:
                raise KeyError(
                    f"Key '{key}' not found in category '{category}' of {filename}."
                )
        else:
            raise KeyError(f"Category '{category}' not found in {filename}.")
    except FileNotFoundError:
        raise FileNotFoundError(f"The configuration file '{filename}' does not exist.")
    except configparser.Error as e:
        # Handle other potential configparser exceptions
        print(f"An error occurred while reading the configuration: {e}")


def config_list(category, key):
    """
    Convert a string representation of a list to an actual list,
    removing leading and trailing whitespace from each element.

    Parameters:
        input_string (str): String representation of a list

    Returns:
        list: List containing the elements parsed from the input string
    """
    # Remove curly braces and split the string by commas
    items = config(category, key).strip("{}").split(",")

    # Strip leading and trailing whitespace from each element and return the list
    return [item.strip() for item in items]
