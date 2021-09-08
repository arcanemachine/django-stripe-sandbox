import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


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
def get_setting(val, default=None, cast=str, show_warning=False):
    """
    Get setting from environment variable, local_config, or default.
    Settings are prioritized in the above order.
    """
    env_result = None
    lc_result = None
    if os.environ.get(f'DJANGO_{val}'):
        # check environment variables
        env_result = os.environ[f'DJANGO_{val}']
    try:
        # check local_config.py
        from . import local_config  # noqa: 401
        lc_result = eval(f"local_config.{val}")
        if env_result:
            # if setting exists in environment variable and local_config.py,
            # then use the environment variable value
            message = f"\n{val} has been set in both environment variable "\
                "and local_config.py.\n"\
                f"Using environment variable value ({val} = {env_result})\n"
            print(colorize(message))
            return cast(env_result)
        else:
            return lc_result
    except (ImportError, AttributeError):
        if show_warning and not env_result:
            # show warning in the console
            if val == 'SECRET_KEY':
                message = "\nWarning: You are using the default SECRET_KEY. "\
                    "If this application is accessible over the Internet, "\
                    "you should create a new SECRET_KEY before continuing."
                print(colorize(message, "red"))
            elif val == 'DEBUG':
                message = f"\nNote: You have not set a value for DEBUG, "\
                      f"so it has been set to a default value of {default}.\n"
                print(colorize(message))
            else:
                quote_mark = "'" if cast == str else ''
                message = f"\nNote: You have not set a value for "\
                    f"settings.{val}, so it has been set to a default value "\
                    f"of {quote_mark}{default}{quote_mark}.\n"
                print(colorize(message))
        # return default value if env_result not found
        return cast(env_result) if env_result else default
