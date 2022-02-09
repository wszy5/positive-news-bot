from scraper import main_news,video_news,health_news
import telebot
import random
import os
from telebot import types
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("APIkey")

bot = telebot.TeleBot(API_KEY)

def make_default_keyboard():
    """Makes default KeyBoard"""
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.InlineKeyboardButton(text='/Popularne', )
    itembtn2 = types.InlineKeyboardButton(text='/Wideo', )
    itembtn3 = types.InlineKeyboardButton(text='/Zdrowie', )
    itembtn4 = types.InlineKeyboardButton(text='/info', )
    markup.add(itembtn1, itembtn2,itembtn3,itembtn4)
    return markup

@bot.message_handler(commands=['Popularne'])
def send_random_news(message):
    arr = main_news()
    random_news = random.choice(arr)
    bot.send_message(message.chat.id,random_news,reply_markup=make_default_keyboard())

@bot.message_handler(commands=['Wideo'])
def send_video_news(message):
    arr = video_news()
    news = random.choice(arr)
    bot.send_message(message.chat.id,news,reply_markup=make_default_keyboard())

@bot.message_handler(commands=['Zdrowie'])
def send_video_news(message):
    arr = health_news()
    news = random.choice(arr)
    bot.send_message(message.chat.id,news,reply_markup=make_default_keyboard())

@bot.message_handler(commands=['start'])
@bot.message_handler(commands=['info'])
def send_about(message):
    msg = "Bot pobiera artykuły ze strony dobrewiadomosci.net.pl\nAutor: Wiktor Szymański"
    bot.send_message(message.chat.id,msg,reply_markup=make_default_keyboard())


bot.polling()

