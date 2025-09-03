from aiogram import Router

from aiogram.filters import Command
from aiogram.types import Message
from utils.database.create_db import SqlLite
from bot import bot
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.state import State, StatesGroup


router = Router()
admin_id = 502419529

db = SqlLite()


class Form(StatesGroup):
    telegram_id = State()


@router.message(Command("search"))
async def private(message: Message, state: FSMContext):
    if message.from_user.id != admin_id:
        await message.answer("Вы не админ")
        return
    await state.set_state(Form.telegram_id)  # Устанавливаем состояние Form.name
    await message.answer("Ведите id")


@router.message(Form.telegram_id)
async def search_by_id(message: Message):
    messages = db.get_user_messages_by_id(user_id=message.text)
    if not messages:
        message.answer("Not found user")
    else:
        for mes_id, chat_id in messages:
            await bot.forward_message(
                chat_id=message.chat.id, from_chat_id=chat_id, message_id=mes_id
            )


@router.message(Command('delete'))
async def delete_message(message: Message):
    if message.from_user.id != admin_id:
        await message.reply("Вы не админ")
        return
    elif not message.reply_to_message:
        await message.reply('Сообщение не найдено')
    else:
        origin_message = message.reply_to_message
        await bot.delete_message(chat_id=origin_message.chat.id, message_id=origin_message.message_id)
        await message.delete()
