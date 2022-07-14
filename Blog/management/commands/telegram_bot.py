import telebot
from telebot import types, util
import logging
from django.conf import settings
from Blog.models import Post
import time

logger = telebot.logger
telebot.logger.setLevel(logging.INFO)

bot = telebot.TeleBot(settings.TELEGRAM_TOKEN, parse_mode=None)

@bot.message_handler(commands=['posts'])
def send_welcome(message):
    for post in Post.objects.all()[:10:]:
        bot.send_message(message.chat.id, f"Title: {post.title}\nPublish: {post.publish_at}")
        time.sleep(1)

@bot.message_handler(commands=['add_post'])
def add_post(message):
    # /add_post Big Text
    data = util.extract_arguments(message.text)

    title = data[:10:]
    text = data

    new_post = Post()
    new_post.title = title
    new_post.text = text
    new_post.save()

    bot.send_message(message.chat.id, f"Title: {new_post.title}\nPublish: {new_post.publish_at}")

bot.infinity_polling()