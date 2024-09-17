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
        for enemy in range(1, self.enemies + 1):
            if enemy % self.power == 0:
                days += 1
                sleep(1)
                print(
                    f"{self.name} сражается {days} дней(дня)..., осталось {self.enemies - self.power * days} воинов."
                )
        print(f"{self.name} одержал победу спустя {days} дней(дня)!")


# Создание класса
first_knight = Knight("Sir Lancelot", 10)
second_knight = Knight("Sir Galahad", 20)
# Запуск потоков и остановка текущего
first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()
print("Все битвы закончились!")
# Вывод строки об окончании сражения
