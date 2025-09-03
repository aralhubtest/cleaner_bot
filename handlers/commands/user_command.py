from aiogram import Router, html

from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from utils.database.create_db import SqlLite
from utils.database.schema import User
router = Router()
db = SqlLite()

@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    user = db.get_user_by_username(username=message.from_user.username)
    if not user:
        db.add_to_user(user=User(
            id=message.from_user.id,
            first_name=message.from_user.first_name,
            last_name=message.from_user.last_name,
            username=message.from_user.username
        ))
        await message.answer("Hello, you added to db")
    else:
        await message.answer(f"Hello, {html.bold(user[1])} your id = {user[0]}.")


@router.message(Command("help"))
async def help_handler(message: Message) -> None:
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!, Help H")

