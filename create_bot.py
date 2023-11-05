from aiogram import Bot, Dispatcher

from core.config import Config, load_config

config: Config = load_config()
bot: Bot = Bot(token=config.BOT_TOKEN, parse_mode="HTML")
dp: Dispatcher = Dispatcher()