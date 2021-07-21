"""Прийом"""

import json
from main import create_ord_rabbit
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
    'localhost',
    credentials=pika.PlainCredentials("admin", "password")
    ))
channel = connection.channel()


channel.queue_declare(queue='Create')

""" Формат JSON:
        {
        "customer":(id клиента - целое число),
        "status":(Статус заявки - строка),
        "type":(Тип заявки - строка),
        "descript":(Описание заявки - строка),
        "serial":(Серийый номер устройства - строка илицелое число),
        "price":(цена заявки - целое число),
        "creator":(id создателя заявки - целое число)
        }
        """


def callback(*args):
    a = json.loads(args[3].decode("utf-8").replace("'", '"'))
    create_ord_rabbit(a)


channel.basic_consume(queue="Create", on_message_callback=callback, auto_ack=True)
channel.start_consuming()
