## 1. Установить python

3.10+ версию (https://www.python.org/downloads/)

проверить через:
    ```
    python3 --version
    ```

## 2. Клонировать проект

через git: 
    ```
    git clone https://github.com/AporiaPD/whos-home-telegram-bot.git
    ```
    
открыть проект:
    ```
    cd whos-home-telegram-bot
    ```

## 3. Создать виртуальное окружение
venv:
    ```
    python3 -m venv venv
    ```

## 4. Активировать виртуальное окружение:
для Windows:
    ```
    venv/Scripts/activate
    ```
    
для Mac/Linux: 
    ```
    source venv/bin/activate
    ```

## 5. Установить зависимости:
из файла _**requirements.txt**_
    ```
    pip install -r requirements.txt
    ```

## 6. Настроить окружение:
в корне проекта создать файл _**.env**_

пример содержимого _**.env**_ файла: (Как в _**.env.example.**_) 
```
    BOT_TOKEN = '123123:AAFFdfgEv8dfgfdg1fdgAEodfgaViW7g'
    ADMIN_CHAT_ID = '-10123123123123'
```
```
    BOT_TOKEN - Токен Вашего бота
    ADMIN_CHAT_ID - ID чата администраторов
```

## 7. Запустить бота:
через _**bot.py**_
    ```
    python bot.py
    ```
