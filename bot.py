from scraper import main_news
import telebot
import random
import os

good_api_key = os.getenv("good_api_key")

bot = telebot.TeleBot(good_api_key,parse_mode=None)

@bot.message_handler(commands=['daj'])
def send_random_news(message):
    arr = main_news()
    random_news = random.choice(arr)
    arr.remove(random_news)
    bot.send_message(message.chat.id,random_news)

@bot.message_handler(commands=['autor'])
def send_about(message):
    bot.send_message(message.chat.id,'Bota stworzył Wiktor Szymański')


bot.polling()

