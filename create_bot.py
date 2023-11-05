from aiogram import Bot, Dispatcher

from core.config import Config, load_config

config: Config = load_config(".env")
bot: Bot = Bot(token=config.tg_bot.BOT_TOKEN, parse_mode="HTML")
dp: Dispatcher = Dispatcher()
