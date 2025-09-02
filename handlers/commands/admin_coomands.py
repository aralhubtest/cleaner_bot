from aiogram import Router

from aiogram.filters import Command
from aiogram.types import Message
from utils.database.create_db import SqlLite
from bot import bot

router = Router()
admin_id = 502419529

db = SqlLite()


@router.message(Command("admin"))
async def private(message: Message):
    if message.from_user.id != admin_id:
        await message.answer("Вы не админ")
        return
    await message.answer("Hello this is private")
    messages = db.get_messages()
    for mes_id, chat_id, text in messages:
        await bot.forward_message(
            chat_id=message.chat.id, from_chat_id=chat_id, message_id=mes_id
        )
