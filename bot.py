import asyncio
import logging

from create_bot import bot, dp
from core.handlers import router


logger = logging.getLogger(__name__)


async def run_bot() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(filename)s:%(lineno)d #%(levelname)-8s "
        "[%(asctime)s] - %(name)s - %(message)s",
    )

    dp.include_router(router)

    logger.info("Start bot")

    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(run_bot())
    except (KeyboardInterrupt, SystemExit):
        logger.info("Bot stopped")
