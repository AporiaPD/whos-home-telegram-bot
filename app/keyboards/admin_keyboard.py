from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def take_req_kb(request_id: str):
    keyboard=InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='Взять', callback_data=f'take:{request_id}')]
        ]
    )
    return keyboard
