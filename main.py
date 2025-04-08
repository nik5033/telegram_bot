import telebot
from config import API_WEATHER, API_TOKEN
from handlers.commands import register_handlers

bot = telebot.TeleBot(API_TOKEN)

def main():
    bot = telebot.TeleBot(API_TOKEN)
    register_handlers(bot)
    bot.infinity_polling()

if __name__ == "__main__":
    main()