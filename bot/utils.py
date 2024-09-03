from aiogram import Bot
from aiogram.types import BotCommand
import requests
import logging
from configurator import config
from messages import ERROR_API, ERROR_INTERNAL, ERROR_NOT_FOUND


async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="start", description="Запустить / Перезапустить бота.")
    ]

    await bot.set_my_commands(commands)


def get_temp(query: str):
    key = config.api_key.get_secret_value()
    url = f"http://api.weatherapi.com/v1/current.json?key={key}&q={query}&lang=ru"

    response = requests.get(url=url)
    data = response.json()

    if "error" not in data:
        return {
            "time": data["location"]["localtime"],
            "weather": data["current"]["condition"]["text"],
            "temp": data["current"]["temp_c"],
            "temp_like": data["current"]["feelslike_c"],
        }
    else:
        code = data["error"]["code"]

        if code == 1006:
            raise Exception(ERROR_NOT_FOUND)
        elif code == 9999:
            logging.error("API ERROR. CODE 9999.")
            raise Exception(ERROR_INTERNAL)
        else:
            logging.error(f"API ERROR. CODE {code}.")
            raise Exception(ERROR_API)
