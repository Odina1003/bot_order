from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpRequest, HttpResponse
import telebot
from .control import bot
import logging

@bot.message_handler(commands=['start'])
def say_hello(message):
    bot.send_message(message.chat.id,'Hello!..')

@csrf_exempt
def index(request: HttpRequest):
    if request.method =='GEt':
        return HttpResponse('Telegram Bot')
    if request.method == 'POST':
        update = telebot.types.Update.de_json(
            request.body.decode("utf-8"))
        try:
            bot.process_new_updates([update])
        except Exception as e:
            logging.error(e)
        return HttpResponse(status=200)