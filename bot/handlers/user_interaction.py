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
                time=data["time"],
                weather=data["weather"],
                temp=data["temp"],
                temp_like=data["temp_like"],
            )
        )

    except Exception as e:
        await message.answer(f"{e}")


@router.message(F.content_type == "location")
async def send_weather_by_location(message: Message):
    try:
        latitude = message.location.latitude
        longtude = message.location.longitude

        user_location = f"{latitude},{longtude}"
        data = get_temp(user_location)

        await message.answer(
            WEATHER_ANSWER.format(
                time=data["time"],
                weather=data["weather"],
                temp=data["temp"],
                temp_like=data["temp_like"],
            )
        )

    except Exception as e:
        await message.answer(f"{e}")
