import pika
from pika import PlainCredentials

connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost', credentials=PlainCredentials("admin", "password")))

channel = connection.channel()

channel.queue_declare(queue='Create')


def send_message(message):
    channel.basic_publish(exchange='', routing_key='Create', body=message)


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

send_message(str({
                    "customer": 1,
                    "status": "Новый",
                    "type": "Платный",
                    "descript": "сломана антена",
                    "serial": 666,
                    "price": 0,
                    "creator": 1}))
connection.close()
