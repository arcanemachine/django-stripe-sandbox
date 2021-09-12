import logging
import os
from dotenv import load_dotenv, dotenv_values
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv()


def colorize(message, color="yellow"):
    color_code_white = '\033[0m'

    if color == "red":
        color_code = '\033[31m'
    elif color == "yellow":
        color_code = '\033[33m'
    elif color == "green":
        color_code = '\033[32m'
    else:
        print("Invalid color specified. Using white...")
        color_code = color_code_white

    return(f"{color_code}{message}{color_code_white}")


# settings
def setting_get(val, default=None, cast=str, show_warning=False):
    """
    Get setting from dotenv, environment variable, local_config, or default.
    Settings are prioritized in the order given above.
    """
    logger = logging.getLogger(__name__)

    dotenv_result = None  # dotenv file
    os_env_result = None  # environment variable
    local_config_result = None  # local_config
    val_exists_in_locations = []

    quote_mark = "'" if cast == str else ''  # used for quoting string values

    # check dotenv file
    if val in dotenv_values('.env'):
        dotenv_result = cast(dotenv_values('.env')[val])
        val_exists_in_locations.append('dotenv')
    elif os.environ.get(f'{val}'):
        # if value not present in dotenv file, check environment variables
        os_env_result = os.environ[f'{val}']
        val_exists_in_locations.append('os_env')
    try:
        # check local_config.py
        from . import local_config  # noqa: 401
        local_config_result = eval(f"local_config.{val}")
        val_exists_in_locations.append('local_config')
    except (ImportError, AttributeError):
        # if value not found, warn the user (if applicable)
        if show_warning:
            if val == 'SECRET_KEY':
                print("\nWarning: You are using the default SECRET_KEY. "
                      "For security purposes, this is not recommended.\n")
            elif val == 'DEBUG':
                print(f"\nNote: You have not set a value for DEBUG, "
                      f"so it has been set to a default value of {default}.\n")
            else:
                print(f"\nNote: You have not set a value for settings.{val}, "
                      "so it has been set to a default value of "
                      f"{quote_mark}{default}{quote_mark}.\n")

    # if value is set in multiple locations, log a warning
    if len(val_exists_in_locations) > 1:
        logger.warning(f"\n{val} set in multiple locations: "
                       f"{', '.join(val_exists_in_locations)}. "
                       f"Using value from {val_exists_in_locations[0]}.\n")

    # return results in expected order
    try:
        return cast(dotenv_result) if dotenv_result \
            else cast(os_env_result) if os_env_result \
            else local_config_result if local_config_result \
            else default
    except ValueError:
        logger.warning(
            f"\n{val} is not type {cast.__name__}. Using default...")
        return default
