import logging
from aiogram import Router, F
from aiogram.types import Message

from utils.database.schema import User, Chat, Message as MS
from utils.database.create_db import SqlLite
from utils.funcs import contains_words
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
        logging.info(message.chat.type)
        chat = Chat(
                id=message.chat.id,
                type=message.chat.type,
                title=message.chat.title,
                username=message.chat.username
            )
        user = User(
                id=message.from_user.id,
                first_name=message.from_user.first_name,
                last_name=message.from_user.last_name,
                username=message.from_user.username,
            )
        if db.get_user_by_id(message.from_user.id):
            pass
        else:
            db.add_to_user(user=user)

        if db.check_group(message.chat.id):
            pass
        else:
            db.add_to_chat(
                chat=chat
            )
        db.create_message(
            message=MS(
                id=message.message_id,
                user_id=user.id,
                group_id=chat.id,
                text=message.text
            )
        )
        logging.info(message.text)
        if contains_words(message.text):
            message.delete()

    except TypeError as e:
        logging.error(e)
        await message.answer("Nice try!")
