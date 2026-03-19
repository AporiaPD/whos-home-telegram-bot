# FSM - Finite State Machine
from aiogram.fsm.state import State, StatesGroup

class UserSatate(StatesGroup):
    waiting_arrival = State()
    waiting_duration = State()
