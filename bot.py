import telebot
import os
from dotenv import load_dotenv 

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
START_MESSAGE = os.getenv("START_MESSAGE")
STIKER_ID = os.getenv("STIKER_ID")

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])

def start(message):

    bot.send_message(message.chat.id , START_MESSAGE)
    bot.send_sticker(chat_id=message.chat.id, sticker=STIKER_ID)

bot.infinity_polling()