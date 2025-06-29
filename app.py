import os
import telebot
from flask import Flask, request

bot = telebot.TeleBot(os.environ['TELEGRAM_TOKEN'])
app = Flask(__name__)

# Komendy bota
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Cześć! Jestem Twoim Diogenesem w beczce. Szukasz prawdy?")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    if "beczk" in message.text.lower():
        bot.reply_to(message, "🛢️ *Stuk w beczkę* 🛢️\nDiogenes odpowiada: 'Szukam uczciwego człowieka!'", parse_mode='Markdown')
    else:
        bot.reply_to(message, "Mów krótko jak Diogenes!")

# Webhook dla Heroku
@app.route('/' + os.environ['TELEGRAM_TOKEN'], methods=['POST'])
def get_message():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200

@app.route('/')
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='
