from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message

from messages import START, WEATHER_ANSWER
from utils import get_temp

router = Router()
router.message.filter(F.chat.type.in_(["private"]))


@router.message(Command("start"))
async def command_start(message: Message):
    await message.answer(START)


@router.message(F.text)
async def send_weather_by_city(message: Message):
    try:
        data = get_temp(message.text)

        await message.answer(
            WEATHER_ANSWER.format(
                city=data["city"],
                time=data["time"],
                weather=data["weather"],
                temp=data["temp"],
                temp_like=data["temp_like"],
            )
        )

    except Exception:
        # TODO усовершеснтвовать для более понятного ответа + логирование.
        await message.answer("Упс. Кажется, что-то пошло не так.")
