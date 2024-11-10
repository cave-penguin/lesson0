from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from aiogram.utils import executor

from crud_functions import get_all_products

api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="Рассчитать"),
        KeyboardButton(text="Информация")
    ],
    [KeyboardButton(text='Купить')]
],
    resize_keyboard=True)

inline_kb = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton(text="Рассчитать норму калорий",
                                 callback_data="calories"),
            InlineKeyboardButton(text="Формулы расчёта",
                                 callback_data="formulas")
        ]
    ]
)

products = get_all_products()

inline_menu = InlineKeyboardMarkup()
for product in products:
    button = InlineKeyboardButton(text=f'{product[1]} {product[0]}',
                                  callback_data=f'product_buying_{product[0]}')
    inline_menu.add(button)


def calc_calories(age, growth, weight):
    return 10 * float(weight) + 6.25 * float(growth) - 5 * float(age) + 5


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(commands="start")
async def start(message: types.Message):
    await message.answer("Привет! Я бот помогающий твоему здоровью.",
                         reply_markup=kb)


@dp.message_handler(text="Рассчитать")
async def main_menu(message):
    await message.answer("Выберите опцию:", reply_markup=inline_kb)


@dp.callback_query_handler(text="formulas")
async def get_formulas(call):
    await call.message.answer(
        "10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5")
    await call.answer()


@dp.callback_query_handler(text="calories")
async def set_age(call):
    await call.message.answer("Введите свой возраст:")
    await UserState.age.set()
    await call.answer()


@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    await state.update_data(user_age=message.text)
    await message.answer("Введите свой рост:")
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    await state.update_data(user_growth=message.text)
    await message.answer("Введите свой вес:")
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    await state.update_data(user_weight=message.text)
    data = await state.get_data()
    result = calc_calories(data["user_age"], data["user_growth"],
                           data["user_weight"])
    await message.answer(f"Норма составляет {result} калорий", reply_markup=kb)
    await state.finish()


@dp.message_handler(text='Купить')
async def get_buying_list(message):
    photos = [f'files/{num}png.png' for num in range(1, 5)]
    for prod in products:
        for photo in photos:
            index = int(''.join([i for i in photo if i.isdigit()]))
            if prod[0] == index:
                await message.answer(f"Название: {prod[1]} {prod[0]} | "
                                     f"Описание: "
                                     f"{prod[2]} | Цена:"
                                     f" {prod[3]}")
                with open(photo, 'rb') as img:
                    await message.answer_photo(img)
    await message.answer(text="Выберите продукт для покупки: ",
                         reply_markup=inline_menu)


for product in products:
    @dp.callback_query_handler(text=f'product_buying_{product[0]}')
    async def send_confirm_message(call, prod=product):
        await call.message.answer(
            f"Вы успешно приобрели продукт {prod[1]} {prod[0]}!")
        await call.answer()


@dp.message_handler()
async def all_messages(message: types.Message):
    await message.answer("Введите команду /start, чтобы начать общение.")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

