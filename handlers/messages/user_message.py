import logging
from aiogram import Router, F
from aiogram.types import Message

from utils.database.schema import User
from utils.database.create_db import SqlLite

logger = logging.getLogger(__name__)


router = Router()
db = SqlLite()


async def filter_system_ms(message: Message):
    if message.new_chat_members:
        return True
    elif message.left_chat_member:
        return True
    elif message.new_chat_title:
        return True
    elif message.new_chat_photo:
        return True
    elif message.delete_chat_photo:
        return True
    else:
        return False


@router.message()
async def echo_handler(message: Message) -> None:
    try:
        logging.info(message.new_chat_members)
        if await filter_system_ms(message=message):
            await message.delete()
        user = User(
            id=message.from_user.id,
            first_name=message.from_user.first_name,
            last_name=message.from_user.last_name,
            username=message.from_user.username,
        )
        await db.add_to_user(user=user)
    except TypeError:
        await message.answer("Nice try!")
