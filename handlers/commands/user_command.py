from aiogram import Router, html

from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from utils.database.insert_to_db import add_to_user, get_user_by_username

router = Router()


@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    user = get_user_by_username(username=message.from_user.username)
    if not user:
        add_to_user(message.from_user.username, message.from_user.full_name)
        await message.answer("Hello, you added to db")
    else:
        await message.answer(f"Hello, {html.bold(user[1])} your id = {user[0]}.")


@router.message(Command("help"))
async def help_handler(message: Message) -> None:
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!, Help H")
