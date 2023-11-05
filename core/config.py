from pydantic import BaseSettings

from dotenv import load_dotenv


class Config(BaseSettings):
    BOT_TOKEN: str


def load_config() -> Config:
    load_dotenv("..env")
    return Config()
