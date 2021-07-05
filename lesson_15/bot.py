import datetime

from telebot import TeleBot
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
app = Flask("__bot__")
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost/postgres"
db = SQLAlchemy(app)

x = "1772461411:AAGpWy5vDHgvw0lOpqegfV0tY7BUu-XIgQs"
bot = TeleBot(token=x)

class BotUsers(db.Model):
    di = db.Column(db.Integer, primary_key=True)
    nick = db.Column(db.String(50), nullable=False)
    chat_id = db.Column(db.Integer, nullable=False)
    mess_time = db.Column(db.DateTime, nullable=False)

@bot.message_handler(commands=['start'])
def start(m):
    bot.send_message(chat_id=m.chat.id, text=f'Здравствуйте {m.chat.username}.\nВозможности бота:')
    bot.send_message(chat_id=m.chat.id, text='Подписатся:\n/subsribe ')

@bot.message_handler(commands=['subsribe'])
def subscribe(m):
    x = BotUsers(
        nick=m.chat.username,
        chat_id=m.chat.id,
        mess_time=datetime.datetime.now()
    )
    db.session.add(x)
    db.session.commit()
    bot.send_message(chat_id=m.chat.id, text=f'Вы подписаны на рассылку уведомлений о готовности заявок. ID = {x.di}')



bot.polling()