from scraper import main_news
import telebot
import random
import os
from telebot import types

api_key = os.getenv("api_key")
bot = telebot.TeleBot(api_key,parse_mode=None)

def make_default_keyboard():
    """Makes default KeyBoard"""
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.InlineKeyboardButton(text='/daj', )
    itembtn2 = types.InlineKeyboardButton(text='/autor', )
    markup.add(itembtn1, itembtn2)
    return markup

@bot.message_handler(commands=['daj'])
def send_random_news(message):
    arr = main_news()
    random_news = random.choice(arr)
    arr.remove(random_news)
    bot.send_message(message.chat.id,random_news,reply_markup=make_default_keyboard())

@bot.message_handler(commands=['autor'])
def send_about(message):
    bot.send_message(message.chat.id,'Bota stworzył Wiktor Szymański',reply_markup=make_default_keyboard())


bot.polling()

