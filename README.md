## 1. Установить python 

3.10+ версию (https://www.python.org/downloads/)

Проверить через:
    ```
    python3 --version
    ```

## 2. Клонировать проект

Через git:
    ```
    git clone https://github.com/AporiaPD/whos-home-telegram-bot.git
    ```

Открыть проект:
    ```
    cd whos-home-telegram-bot
    ```

## 3. Создайть виртуальное окружение

Виртуальное окружение:
    ```
    python3 -m venv venv
    ```

## 4. Активировать виртуальное окружение

Для Windows:
    ```
    venv/Scripts/activate
    ```

Для Mac/Linux:
    ```
    source venv/bin/activate
    ```

## 5. Установить зависимости:

Из файла _**requirements.txt**_:
    ```
    pip install -r requirements.txt
    ```
## 6. Настроить окружение
Создать _**.env**_ файл в корне проекта

Пример содержимого (Как в _**.env.example.**_):
```
BOT_TOKEN = '123123:AAFFdfgEv8dfgfdg1fdgAEodfgaViW7g'
ADMIN_CHAT_ID = '-10123123123123'
```
    
**BOT_TOKEN** - Токен Вашего бота, полученный через BotFather

**ADMIN_CHAT_ID** - ID чата администраторов

## 7. Запустить бота:
Через _**bot.py**_:
    ```
    python bot.py
    ```
