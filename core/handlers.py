import logging

from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from .states import RequestBotState


router = Router()

logger = logging.getLogger(__name__)


@router.message(Command("start"))
async def start_command(message: types.Message, state: FSMContext):
    await message.delete()
    await message.answer("start button was tapped")
    await state.set_state(state=RequestBotState.main_state)


@router.message(Command("help"))
async def start_command(message: types.Message, state: FSMContext):
    await message.delete()
    await message.answer("help button was tapped")
    await state.set_state(state=RequestBotState.main_state)


@router.message()
async def echo(message: types.Message, state: FSMContext):
    text = message.text
    await message.reply(text=text)
    await state.set_state(state=RequestBotState.main_state)
