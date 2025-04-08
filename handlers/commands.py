from requests import get
from config import API_WEATHER
import json

def register_handlers(bot):
    @bot.message_handler(commands=['start'])
    def start_handler(message):
        bot.reply_to(message, f'Hi {message.from_user.first_name}')

    @bot.message_handler(commands=['weather'])
    def weather_handler(message):
        bot.send_message(message.from_user.id, 'Введите город:')
        bot.register_next_step_handler(message, get_city)

    def parse_json(json_data):
        temp = json_data['main']['temp']
        temp_like = json_data['main']['feels_like']
        pressuse = json_data['main']['pressure']
        wind_speed = json_data['wind']['speed']

        result_str = f'Температура: {temp}\n \
                    Чувствуется как: {temp_like}\n \
                    Давление: {pressuse}\n \
                    Скорость ветра: {wind_speed}'
        
        return result_str

    def get_city(message):
        city = message.text

        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_WEATHER}&lang=ru'
        responce = get(url)

        parsed_json = parse_json(json.loads(responce.text))

        bot.send_message(message.from_user.id, parsed_json)