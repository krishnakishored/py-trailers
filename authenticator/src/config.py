import logging
import os
from functools import lru_cache

# from typing import ClassVar
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv(verbose=True)  # with increased verbosity


class TokenSettings(BaseSettings):

    SECRET_KEY: str = (
        "your_secret_key"  # Use a more secure key and keep it secret!
    )
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30


class Settings(TokenSettings):
    HOST: str = "0.0.0.0"
    PORT: int = 8010
    APP_NAME: str = "authenticator"
    APP_VERSION: str = os.environ.get("APP_VERSION", "0.0.0.1")
    APP_DESCRIPTION: str = os.environ.get(
        "APP_DESCRIPTION",
        "Authenticator service for user authentication and authorization",
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
