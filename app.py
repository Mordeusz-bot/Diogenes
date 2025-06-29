import os
import telebot
from flask import Flask, request

bot = telebot.TeleBot(os.environ['TELEGRAM_TOKEN'])
app = Flask(__name__)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "🛢️ Diogenes says: 'I search for an honest bot user!'")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, "Speak briefly, philosopher!")

@app.route('/' + os.environ['TELEGRAM_TOKEN'], methods=['POST'])
def webhook():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200

if __name__ == '__main__':
    bot.remove_webhook()
    bot.set_webhook(url='https://YOUR-APP-NAME.herokuapp.com/' + os.environ['TELEGRAM_TOKEN'])
    app.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
