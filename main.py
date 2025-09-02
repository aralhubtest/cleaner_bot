import asyncio
import logging
import sys

from aiogram import Dispatcher
from middlewares.middleware import MyLoggingMiddleware
from handlers.commands.admin_coomands import router as admin_command
from handlers.commands.user_command import router as user_command
from handlers.messages.user_message import router as user_message
from utils.database.create_db import SqlLite
from bot import bot


dp = Dispatcher()
dp.message.middleware(MyLoggingMiddleware())
dp.include_router(admin_command)
dp.include_router(user_command)
dp.include_router(user_message)


async def main() -> None:
    db = SqlLite()
    db.create_db()
    db.down()
    # Initialize Bot instance with default bot properties which will be passed to all API calls

    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
