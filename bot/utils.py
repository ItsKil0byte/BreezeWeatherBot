from aiogram import Bot
from aiogram.types import BotCommand
import requests
from configurator import config


async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="start", description="Запустить / Перезапустить бота.")
    ]

    await bot.set_my_commands(commands)


def get_temp(city: str):
    key = config.api_key.get_secret_value()
    url = f"http://api.weatherapi.com/v1/current.json?key={key}&q={city}&lang=ru"

    response = requests.get(url=url)

    if response.status_code == 200:
        data = response.json()
        return {
            "city": data["location"]["name"],
            "time": data["location"]["localtime"],
            "weather": data["current"]["condition"]["text"],
            "temp": data["current"]["temp_c"],
            "temp_like": data["current"]["feelslike_c"],
        }
    else:
        raise Exception
