import logging

from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from .states import RequestBotState
from .services import get_order_data, is_valid_uuid, get_message_text, has_access
from .message_texts import HELLO_TEXT, WRONG_FORMAT_TEXT, WRONG_USER_TEXT, HELP_TEXT


router = Router()

logger = logging.getLogger(__name__)


@router.message(Command("start"))
async def start_command(message: types.Message, state: FSMContext):
    user_id = str(message.from_user.id)
    try:
        user_name = message.from_user.full_name
    except Exception as error:
        logger.info(f"something went wrong: {error}")
        user_name = user_id
    user_has_access = await has_access(user_id)
    await message.delete()
    if user_has_access:
        await message.answer(text=HELLO_TEXT.format(user_name=user_name))
    else:
        await message.answer(text=WRONG_USER_TEXT)
    await state.set_state(state=RequestBotState.main_state)


@router.message(Command("help"))
async def start_command(message: types.Message, state: FSMContext):
    user_id = str(message.from_user.id)
    await message.delete()
    user_has_access = await has_access(user_id)
    if user_has_access:
        await message.answer(text=HELP_TEXT)
    else:
        await message.answer(text=WRONG_USER_TEXT)
    await state.set_state(state=RequestBotState.main_state)


@router.message()
async def echo(message: types.Message, state: FSMContext):
    text, user_id = message.text, str(message.from_user.id)
    is_text_uuid = await is_valid_uuid(text)
    user_has_access = await has_access(user_id)
    if user_has_access:
        if is_text_uuid:
            result = await get_order_data(text)
            message_text = await get_message_text(result)
            await message.reply(text=message_text)
        else:
            await message.reply(text=WRONG_FORMAT_TEXT)
    else:
        await message.delete()
        await message.answer(text=WRONG_USER_TEXT)
    await state.set_state(state=RequestBotState.main_state)
