import pika
from django.conf import settings


def send_booking_notification(message):
    params = pika.ConnectionParameters(
        host=settings.RABBITMQ['HOST'],
        port=settings.RABBITMQ['PORT'],
        credentials=pika.PlainCredentials(
            settings.RABBITMQ['USER'],
            settings.RABBITMQ['PASSWORD']
        )
    )
    connection = pika.BlockingConnection(params)
    channel = connection.channel()

    # Объявляем обменник
    channel.exchange_declare(
        exchange=settings.RABBITMQ['EXCHANGE'],
        exchange_type=settings.RABBITMQ['EXCHANGE_TYPE']
    )

    # Объявляем очередь
    channel.queue_declare(queue=settings.RABBITMQ['QUEUE'])

    # Связываем очередь с обменником
    channel.queue_bind(
        exchange=settings.RABBITMQ['EXCHANGE'],
        queue=settings.RABBITMQ['QUEUE'],
        routing_key=settings.RABBITMQ['ROUTING_KEY']
    )

    # Отправляем сообщение в очередь
    channel.basic_publish(
        exchange=settings.RABBITMQ['EXCHANGE'],
        routing_key=settings.RABBITMQ['ROUTING_KEY'],
        body=message
    )
    connection.close()

