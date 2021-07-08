import pika
from pika import PlainCredentials

connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost', credentials=PlainCredentials("admin", "password")))

channel = connection.channel()

channel.queue_declare(queue='Create')


def send_message(message):
    channel.basic_publish(exchange='', routing_key='Create', body=message)


send_message(str({
                    "customer": 1,
                    "status": "Новый",
                    "type": "Платный",
                    "descript": "сломана антена",
                    "serial": 666,
                    "price": 0,
                    "creator": 1}))
connection.close()
