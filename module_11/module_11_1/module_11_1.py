import asyncio
import json
import os
from random import randint

import numpy as np
import requests


async def async_request():
    """
    Делает запрос массива юзеров с сайта и возвращает массив с json объектами
    :return: Возвращает список JSON-объектов (пользователей).
    """
    loop = asyncio.get_event_loop()
    response = await loop.run_in_executor(
        None, requests.get, "https://jsonplaceholder.typicode.com/users/"
    )
    return response.json()


def write_in_file(users, name):
    """
    Записывает в файл при помощи пакета json

    :param users: приходит результат выполнения функции async_request() в виде массива с json объектами
    :param name: приходит название файла куда будут записаны данные
    """
    with open(name, "w", encoding="utf-8") as file:
        json.dump(users, file)


file_name = "./module_11_1/all_users.json"

if not os.path.exists(file_name):
    """
    проверяет есть ли файл с именем file_name, если его нет выполняет код
    """
    all_users = asyncio.run(async_request())
    write_in_file(all_users, file_name)


def get_names(file_name):
    """
    Считывает данные с файла при помощи пакета json и записывает имя как ключ и почтовый индекс как значение словаря

    :param file_name: приходит название файла откуда будут считаны данные
    :return: возвращает список с именем и почтовым индексом
    """
    names_dict = {}
    with open(file_name, encoding="utf-8") as file:
        all_data = json.load(file)
        for user in all_data:
            names_dict[user["name"]] = f"zipcode: {user['address']['zipcode']}"
    return names_dict


names = get_names(file_name)

for key, value in names.items():
    print(f"{key}, {value}")


class UseNumpy:
    """
    Класс для работы с массивами чисел с использованием библиотеки numpy.

    :param amount_of_nums: Количество чисел в массиве.
    :param range_num: Диапазон значений, в котором будут генерироваться случайные числа.
    """

    def __init__(self, amount_of_nums, range_num):
        self.amount_of_nums = amount_of_nums
        self.range_num = range_num
        self.nums = np.array(self.create_list())

    def create_list(self):
        """
        Генерирует список случайных чисел.

        :return: Возвращает список случайных чисел.
        """
        new_list = []
        for i in range(self.amount_of_nums):
            new_list.append(randint(1, self.range_num))
        return new_list

    def calculations(self, condition=None, add_condition=0):
        """
        Выполняет различные операции над массивом чисел.

        :param condition: Условие выполнения операции (например, 'filter', 'sort', 'rsort').
        :param add_condition: Дополнительное условие для фильтрации.
        :return: Возвращает результат операции над массивом.
        """
        match condition:
            case "filter":
                result = self.nums > add_condition
                return self.nums[result]
            case "sort":
                return np.sort(self.nums)
            case "rsort":
                return np.sort(self.nums)[::-1]
            case _:
                return "Не выбрано ни одной операции"


use1 = UseNumpy(200, 100)
print(use1.calculations("filter", 80))
print(use1.calculations("rsort"))
print(use1.calculations("sort"))
print(use1.calculations(100))
print(use1.calculations())
var = UseNumpy.calculations.__doc__
print(var)
