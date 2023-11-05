from aiogram.fsm.state import State, StatesGroup


class RequestBotState(StatesGroup):
    main_state = State()
