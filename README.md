1. Установить python 3.10+ (https://www.python.org/downloads/):
    Проверить через: python3 --version

2. Клонировать проект через git
    git clone https://github.com/AporiaPD/whos-home-bot.git

3. Откройте проект и создайте виртуальное окружение:
    python3 -m venv venv

4. Активировать виртуальное окружение:
    для Windows: 
        venv/Scripts/activate
    для Mac/Linux: 
        source venv/bin/activate

5. Установить зависимости:
    pip install -r requirements.txt

6. Создать и настроить .env файл в корне проекта. Используйте Ваш токен бота и ID чата администраторов.:
    Как в .env.example. Пример содержимого:
        BOT_TOKEN = '123123:AAFFdfgEv8dfgfdg1fdgAEodfgaViW7g'
        ADMIN_CHAT_ID = '-10123123123123'

7. Запуск бота:
    python bot.py