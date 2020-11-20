from scraper import main_news,video_news,health_news
import telebot
import random
import os
from telebot import types
from env import config

bot = telebot.TeleBot(config.api_key,parse_mode=None)

def make_default_keyboard():
    """Makes default KeyBoard"""
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.InlineKeyboardButton(text='/Popularne', )
    itembtn2 = types.InlineKeyboardButton(text='/Wideo', )
    itembtn3 = types.InlineKeyboardButton(text='/Zdrowie', )
    itembtn4 = types.InlineKeyboardButton(text='/Info', )
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


@bot.message_handler(commands=['Info'])
def send_about(message):
    bot.send_message(message.chat.id,'Bota stworzył Wiktor Szymański',reply_markup=make_default_keyboard())


bot.polling()

