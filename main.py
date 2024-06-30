import os

import telebot

API_TOKEN = os.environ['TELEBOT_TOKEN']
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, f'Hi {message.from_user.first_name}')

bot.infinity_polling()