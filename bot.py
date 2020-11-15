import scraper
import telebot
import random
import os
from telebot import types

api_key = os.getenv("api_key")
bot = telebot.TeleBot(api_key,parse_mode=None)

def make_default_keyboard():
    """Makes default KeyBoard"""
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.InlineKeyboardButton(text='/losuj news', )
    itembtn2 = types.InlineKeyboardButton(text='/video news', )
    itembtn3 = types.InlineKeyboardButton(text='/info', )
    markup.add(itembtn1, itembtn2,itembtn3)
    return markup

@bot.message_handler(commands=['losuj news'])
def send_random_news(message):
    arr = main_news()
    random_news = random.choice(arr)
    bot.send_message(message.chat.id,random_news,reply_markup=make_default_keyboard())

@bot.message_handler(commands=['video news'])
def send_video_news(message):
    arr = main_news()
    random_news = random.choice(arr)
    bot.send_message(message.chat.id,random_news,reply_markup=make_default_keyboard())

@bot.message_handler(commands=['info'])
def send_about(message):
    bot.send_message(message.chat.id,'Bota stworzył Wiktor Szymański',reply_markup=make_default_keyboard())


bot.polling()

