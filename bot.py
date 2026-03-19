from aiogram import Bot, Dispatcher
import asyncio

from config import BOT_TOKEN
from app.handlers.user_handler import router as user_router
from app.handlers.admin_handler import router as admin_router


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

async def main():

    # Debug
    print("Bot started!")

    me = bot.get_me()
    print(me)

    # Routers
    dp.include_router(user_router)
    dp.include_router(admin_router)

    # Start
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())