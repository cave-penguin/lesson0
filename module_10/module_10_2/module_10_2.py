from threading import Thread
from time import sleep


class Knight(Thread):
    def __init__(self, name: str, power: int):
        super().__init__()
        self.name = name
        self.power = power
        self.enemies = 100

    def run(self):
        print(f"{self.name}, на нас напали!")
        days = 0
        enemies_count = self.enemies
        while enemies_count > 0:
            enemies_count -= self.power
            days += 1
            sleep(1)
            print(
                f"{self.name} сражается {days} дней(дня)..., осталось {enemies_count if enemies_count > 0 else 0} "
                f"воинов."
            )
        print(f"{self.name} одержал победу спустя {days} дней(дня)!")


# Создание класса
first_knight = Knight("Sir Lancelot", 13)
second_knight = Knight("Sir Galahad", 20)
# Запуск потоков и остановка текущего
first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()
print("Все битвы закончились!")
# Вывод строки об окончании сражения
