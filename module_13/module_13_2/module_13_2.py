from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor

api = "7887074932:AAGWX-FV2p_foXbF05fSXiAHuZ6LN8_zo8g"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands='start')
async def start(message):
    print('Привет! Я бот помогающий твоему здоровью.')

@dp.message_handler()
async def all_messages(message):
    print('Введите команду /start, чтобы начать общение.')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
