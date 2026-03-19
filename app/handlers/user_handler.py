from aiogram import Router
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
import asyncio

from app.states.user_states import UserSatate
from app.keyboards.user_keyboard import arrival_kb
from app.keyboards.admin_keyboard import take_req_kb
from app.services.req_store import create_request
from app.services.req_timeout import expire_request
from config import ADMIN_CHAT_ID

router = Router()

# Start
@router.message(CommandStart())
async def handle_start(message: Message, state: FSMContext):
    user_name = message.from_user.first_name

# --- Время прихода ---
    await message.answer(f'Привет, {user_name}!\n'
                          'Через сколько придёте в Дом архитектора?\n',
                          reply_markup=arrival_kb)
    await state.set_state(UserSatate.waiting_arrival)


@router.message(UserSatate.waiting_arrival)
async def handle_arrival(message: Message, state: FSMContext):
    arrival = message.text
    await state.update_data(arrival=arrival)

# --- Время пребывания ---
    await message.answer('Сколько планируете пробыть?', 
                         reply_markup=ReplyKeyboardRemove())
    await state.set_state(UserSatate.waiting_duration)


@router.message(UserSatate.waiting_duration)
async def handle_duration(message: Message, state: FSMContext):
    duration = message.text
    data = await state.get_data()
    arrival = data["arrival"]

    user = message.from_user
    user_name = user.full_name

    request_id = create_request(user_id=user.id,
                                arrival=arrival,
                                duration=duration)

# --- Отправка заявки администраторам ---
    text = (
         'Гость\n'
        f'{user_name}\n'
        f'Придёт через: {arrival}\n'
        f'Пребывание: {duration}')

    await message.bot.send_message(chat_id=ADMIN_CHAT_ID, 
                                   text=text,
                                   reply_markup=take_req_kb(request_id))

# --- Сообщение в чат пользователю ---
    await message.answer(
        f'Передано администраторам!\n'
         'Ожидайте ответа...\n\n'
        f'Вы придёте через: {arrival} \n'
        f'Пробудете: {duration}')
    
# --- Запуск таймера ---
    asyncio.create_task(expire_request(request_id=request_id, bot=message.bot))

    await state.clear()