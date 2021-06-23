from telebot import TeleBot, types
x = "1772461411:AAGpWy5vDHgvw0lOpqegfV0tY7BUu-XIgQs"
bot = TeleBot(token=x)

@bot.message_handler(commands=['start'])
def start(m):






bot.polling()