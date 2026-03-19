from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

arrival_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='15 мин'),
            KeyboardButton(text='30 мин')
        ],
        [
            KeyboardButton(text='1 час'),
            KeyboardButton(text='1 ч 30 мин')
        ],
        [
            KeyboardButton(text='2 часа') 
        ]
    ],

    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder = "Выберите время Вашего прихода..."
)

# arrival_time = {
#     1: '15 мин',
#     2: '30 мин',
#     3: '1 час',
#     4: '1 ч 30 мин',
#     5: '2 часа'
# }

# arrival_time = [
#     '15 мин',
#     '30 мин',
#     '1 час',
#     '1 ч 30 мин',
#     '2 часа'
# ]