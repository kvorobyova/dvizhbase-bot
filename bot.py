import asyncio
import os

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")


bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start_handler(message: Message):
    name = message.from_user.first_name
    user_id = message.from_user.id

    await message.answer(
        f"Привет, {name}!\n\n"
        f"Telegram ID: {user_id}\n\n"
        "Это все что у нас есть...\n\n"
        "Здесь ща все будет для подготовки к прочим конкурсам"
    )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())