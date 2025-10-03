from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.utils.keyboard import ReplyKeyboardMarkup, KeyboardButton
from aiogram import F
import asyncio
import os

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")  # Токен бота из переменных окружения
bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer("узнать все команды /commands Автор бота - @xeemplee")

    @dp.message(Command("test"))
    async def cmd_test(message: Message):
        await message.answer("раф лох")

        @dp.message(Command("commands"))
        async def cmd_test(message: Message):
            await message.answer("/test - пишет что раф лох /owner - пишет кто владелец бота")

            @dp.message(Command("owner"))
            async def cmd_test(message: Message):
                await message.answer("владелец - @xeemplee")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

