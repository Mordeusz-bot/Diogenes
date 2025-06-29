import os
import telebot
from flask import Flask, request

bot = telebot.TeleBot(os.environ.get('TELEGRAM_TOKEN'))
app = Flask(__name__)

@app.route('/')
def home():
    return "Diogenes Bot is running!", 200

@app.route(f'/{os.environ.get("TELEGRAM_TOKEN")}', methods=['POST'])
def webhook():
    if request.headers.get('content-type') == 'application/json':
        json_str = request.get_data().decode('UTF-8')
        update = telebot.types.Update.de_json(json_str)
        bot.process_new_updates([update])
        return '', 200
    return 'Bad request', 400

if __name__ == '__main__':
    # Remove previous webhook
    bot.remove_webhook()
    # Set new webhook
    bot.set_webhook(url=f'https://YOUR_APP_NAME.herokuapp.com/{os.environ.get("TELEGRAM_TOKEN")}')
    # Run app
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 
