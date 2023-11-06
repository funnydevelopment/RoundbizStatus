import logging

from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from .states import RequestBotState
from .services import get_order_data, is_valid_uuid, get_message_text
from .message_texts import HELLO_TEXT, WRONG_FORMAT_TEXT, WRONG_USER_TEXT
from create_bot import config


router = Router()

logger = logging.getLogger(__name__)


@router.message(Command("start"))
async def start_command(message: types.Message, state: FSMContext):
    user_id = str(message.from_user.id)
    user_name = ""
    try:
        user_name = message.from_user.full_name
    except Exception as error:
        logger.info(f"something went wrong: {error}")
    allowed_users = config.tg_bot.USER_ID.split(",")
    if user_id in allowed_users:
        await message.delete()
        await message.answer(text=HELLO_TEXT.format(user_name=user_name))
    else:
        await message.delete()
        await message.answer(text=WRONG_USER_TEXT)
    await state.set_state(state=RequestBotState.main_state)


@router.message(Command("help"))
async def start_command(message: types.Message, state: FSMContext):
    await message.delete()
    await message.answer("help button was tapped")
    await state.set_state(state=RequestBotState.main_state)


@router.message()
async def echo(message: types.Message, state: FSMContext):
    text = message.text
    is_text_uuid = await is_valid_uuid(text)
    if is_text_uuid:
        result = await get_order_data(text)
        message_text = await get_message_text(result)
        await message.reply(text=message_text)
    else:
        await message.reply(text=WRONG_FORMAT_TEXT)
    await state.set_state(state=RequestBotState.main_state)
