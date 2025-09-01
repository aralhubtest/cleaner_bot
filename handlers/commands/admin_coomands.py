from aiogram import Router

from aiogram.filters import  Command
from aiogram.types import Message

router = Router()
admin_id = 34567890


@router.message(Command('admin'))
async def private(message: Message):
    if message.from_user.id != admin_id:
        await message.answer('Вы не админ')
        return
    await message.answer('Hello this is private')
