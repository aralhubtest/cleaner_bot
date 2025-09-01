import asyncio
import logging
import sys
from os import getenv
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from middlewares.middleware import MyLoggingMiddleware
from handlers.commands.admin_coomands import router as admin_command
from handlers.commands.user_command import router as user_command
from handlers.messages.user_message import router as user_message

load_dotenv()

TOKEN = getenv("BOT_TOKEN")


dp = Dispatcher()
dp.message.middleware(MyLoggingMiddleware())
dp.include_router(admin_command)
dp.include_router(user_command)
dp.include_router(user_message)


async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
