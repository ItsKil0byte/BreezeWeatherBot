START = """
Привет! Я ветерок, и я всегда в курсе погоды.

Хочешь узнать, что творится за окном? 
Напиши мне название города, и я расскажу тебе все подробности!
"""

WEATHER_ANSWER = """
Локация: {location}
Местное время: {time}

Погода: {weather} {icon}
Температура: {temp}
Ощущается как: {temp_like}
"""

ERROR_NOT_FOUND = """
Упс! Я не смог найти информацию по твоему запросу. 
Убедись, что ты правильно написал название города, и попробуй снова!
"""

ERROR_INTERNAL = """
Ой! Кажется, я временно не могу узнать погоду. 
Пожалуйста, попробуй позже — я постараюсь все исправить как можно скорее!
"""

ERROR_API = """
Ой, что-то пошло не так! Возможно, я на технических работах.
Попробуй вернуться немного позже. Я сделаю все, чтобы исправить это как можно быстрее!
"""

CONDITIONS = {
    # NOTE: словарь помогала генерить нейронка с заданными данными погоды и её кода.
    1000: "☀️",  # Sunny
    1003: "🌤️",  # Partly cloudy
    1006: "☁️",  # Cloudy
    1009: "🌥️",  # Overcast
    1030: "🌫️",  # Mist
    1063: "🌦️",  # Patchy rain possible
    1066: "🌨️",  # Patchy snow possible
    1069: "🌧️🌨️",  # Patchy sleet possible
    1072: "🌧️",  # Patchy freezing drizzle possible
    1087: "🌩️",  # Thundery outbreaks possible
    1114: "🌨️💨",  # Blowing snow
    1117: "❄️💨",  # Blizzard
    1135: "🌫️",  # Fog
    1147: "🌫️❄️",  # Freezing fog
    1150: "🌦️",  # Patchy light drizzle
    1153: "🌧️",  # Light drizzle
    1168: "🌧️❄️",  # Freezing drizzle
    1171: "🌧️❄️",  # Heavy freezing drizzle
    1180: "🌦️",  # Patchy light rain
    1183: "🌧️",  # Light rain
    1186: "🌧️",  # Moderate rain at times
    1189: "🌧️",  # Moderate rain
    1192: "🌧️🌧️",  # Heavy rain at times
    1195: "🌧️🌧️",  # Heavy rain
    1198: "🌧️❄️",  # Light freezing rain
    1201: "🌧️❄️",  # Moderate or heavy freezing rain
    1204: "🌧️❄️",  # Light sleet
    1207: "🌧️❄️",  # Moderate or heavy sleet
    1210: "🌨️",  # Patchy light snow
    1213: "🌨️",  # Light snow
    1216: "🌨️",  # Patchy moderate snow
    1219: "🌨️",  # Moderate snow
    1222: "🌨️",  # Patchy heavy snow
    1225: "❄️❄️",  # Heavy snow
    1237: "🌨️",  # Ice pellets
    1240: "🌦️",  # Light rain shower
    1243: "🌧️",  # Moderate or heavy rain shower
    1246: "🌧️🌧️",  # Torrential rain shower
    1249: "🌧️❄️",  # Light sleet showers
    1252: "🌧️❄️",  # Moderate or heavy sleet showers
    1255: "🌨️",  # Light snow showers
    1258: "🌨️❄️",  # Moderate or heavy snow showers
    1261: "🌨️",  # Light showers of ice pellets
    1264: "🌨️❄️",  # Moderate or heavy showers of ice pellets
    1273: "⛈️",  # Patchy light rain with thunder
    1276: "⛈️",  # Moderate or heavy rain with thunder
    1279: "⛈️❄️",  # Patchy light snow with thunder
    1282: "⛈️❄️",  # Moderate or heavy snow with thunder
}
