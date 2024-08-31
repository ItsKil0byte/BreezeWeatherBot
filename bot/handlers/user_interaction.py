from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message

from messages import START

router = Router()
router.message.filter(F.chat.type.in_(["private"]))


@router.message(Command("start"))
async def command_start(message: Message):
    await message.answer(START)
