from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, LinkPreviewOptions

from messages import START, HELP, ABOUT, WEATHER_ANSWER
from utils import get_temp, generate_message

router = Router()
router.message.filter(F.chat.type.in_(["private"]))


@router.message(Command("start"))
async def command_start(message: Message):
    await message.answer(START)


@router.message(Command("help"))
async def command_help(message: Message):
    await message.answer(HELP)


@router.message(Command("about"))
async def command_about(message: Message):
    await message.answer(ABOUT, link_preview_options=LinkPreviewOptions(is_disabled=True))


@router.message(F.text)
async def send_weather_by_city(message: Message):
    try:
        data = get_temp(message.text)
        text = generate_message(WEATHER_ANSWER, data)

        await message.answer(text)

    except Exception as e:
        await message.answer(f"{e}")


@router.message(F.content_type == "location")
async def send_weather_by_location(message: Message):
    try:
        latitude = message.location.latitude
        longtude = message.location.longitude
        user_location = f"{latitude},{longtude}"

        data = get_temp(user_location)
        text = generate_message(WEATHER_ANSWER, data)

        await message.answer(text)

    except Exception as e:
        await message.answer(f"{e}")
