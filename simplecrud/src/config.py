import logging
import os
from functools import lru_cache

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv(verbose=True)  # with increased verbosity


# load_dotenv()
# class DBSettings(BaseSettings):
#     """
#     Database Settings
#     """

#     DB_HOST: str = "database_url"
#     DB_PORT: int = 8185


# class ExternalSettings(BaseSettings):
#     """Third party APIs in use"""

#     FINDER_BASE_URL: str = "https://api.onsonglyrics.com/v1/finder"


class Settings(BaseSettings):
    HOST: str = "0.0.0.0"
    PORT: int = 8020
    APP_NAME: str = "simplecrud"
    APP_VERSION: str = os.environ.get("APP_VERSION", "0.0.0.1")
    APP_DESCRIPTION: str = os.environ.get(
        "APP_DESCRIPTION",
        "A simple CRUD API",
    )
    DEBUG_MODE: bool = False
    # NOTSET=0, DEBUG=10, INFO=20, WARN=30, ERROR=40, CRITICAL=50
    LOG_LEVEL: int = logging.INFO  # info level logs req-resp json

    # in general set DEBUG for dev, WARN for production(least longing)
    class Config:
        # ToDo: Read the urls from environment
        env_file = ".env"  # override the defaults
        # env_file_encoding = 'utf-8'


# @lru_cache() modifies the function it decorates to return the same value that was returned the first time, instead of executing the code every time
@lru_cache()
def get_settings():
    return Settings()


# settings = Settings() #  default instance is not created if 'Depends' is used
