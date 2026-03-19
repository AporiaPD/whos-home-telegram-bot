from aiogram import Router
from aiogram.types import CallbackQuery
from app.services.req_store import get_request, get_requests

router = Router()

@router.callback_query(lambda c: c.data.startswith('take:'))
async def take_request(callback: CallbackQuery):
    request_id = callback.data.split(":")[1].strip()
    request = get_request(request_id)

    if not request: 
        await callback.answer(f"Заявка не найдена", show_alert=True)
        return
    
    if request['status'] == 'expired': 
        await callback.answer(f"Заявка больше не актуальна", show_alert=True)
        return
    
    if request['status'] == 'taken': 
        await callback.answer(f"Заявка уже принята", show_alert=True)
        return

    request['status'] = 'taken'

    admin = callback.from_user
    admin_name = admin.full_name

    user_id = request["user_id"]

# --- Отправка ответа пользователю ---
    await callback.bot.send_message(chat_id=user_id, 
                                   text=f'Ваша заявка принята администратором: {admin_name}')

# --- Сообщение в чат администраторам ---
    admin_text = callback.message.text + f"\n\nЗаявка принята: {admin_name}"
    await callback.answer(f"Вы приняли заявку")
    await callback.message.edit_text(admin_text)