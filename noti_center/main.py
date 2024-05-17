import asyncio
import logging
import os
import sys
from dotenv import load_dotenv
from aio_pika import connect, IncomingMessage
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

load_dotenv()
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

RABBITMQ_HOST = os.getenv('RABBITMQ_HOST')
RABBITMQ_PORT = os.getenv('RABBITMQ_PORT')
RABBITMQ_USER = os.getenv('RABBITMQ_USER')
RABBITMQ_PASSWORD = os.getenv('RABBITMQ_PASSWORD')

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def echo_message(msg: types.Message):
    print(msg.chat.id)
    await msg.answer(msg.chat.id)


async def on_startup(loop):
    # Подключаемся к RabbitMQ и начинаем слушать сообщения
    connection = await connect(f"amqp://{RABBITMQ_USER}:{RABBITMQ_PASSWORD}@{RABBITMQ_HOST}/", loop=loop)
    channel = await connection.channel()  # Создаем канал в RabbitMQ
    queue = await channel.declare_queue('booking_queue')
    await queue.consume(on_message)  # Подписываемся на сообщения из очереди


async def on_message(message: IncomingMessage):
    async with message.process():
        data = message.body.decode()
        await bot.send_message(TELEGRAM_CHAT_ID, text=f"Received message: {data}")


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    loop = asyncio.get_running_loop()
    await on_startup(loop)
    await dp.start_polling(bot)


if __name__ == '__main__':
    # Создаем объекты бота и диспетчера
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
