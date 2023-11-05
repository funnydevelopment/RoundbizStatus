from dataclasses import dataclass

from environs import Env


@dataclass
class Service:
    URL: str
    SHOP_ID: str


@dataclass
class TgBot:
    BOT_TOKEN: str
    USER_ID: str


@dataclass
class Config:
    tg_bot: TgBot
    service: Service


def load_config(path: str = None) -> Config:
    env = Env()
    env.read_env(path)

    return Config(
        tg_bot=TgBot(BOT_TOKEN=env.str("BOT_TOKEN"), USER_ID=env.str("USER_ID")),
        service=Service(URL=env.str("URL"), SHOP_ID=env.str("SHOP_ID")),
    )
