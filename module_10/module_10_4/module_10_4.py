import queue
from random import randint
from threading import Thread, Lock
from time import sleep


class Table:
    def __init__(self, number):
        self.number: int = number
        self.guest = None


class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name: str = name

    def run(self):
        wait = randint(3, 10)
        sleep(wait)


class Cafe:
    def __init__(self, *tables):
        self.q = queue.Queue()
        self.tables = tables
        self.lock = Lock()

    def guest_arrival(self, *guests):
        for g in guests:
            with self.lock:
                available_tables = [
                    table for table in self.tables if table.guest is None
                ]
                if available_tables:
                    table = available_tables.pop(0)
                    table.guest = g
                    g.start()
                    print(f"{g.name} сел(-а) за стол номер {table.number}")
                else:
                    self.q.put(g)
                    print(f"{g.name} в очереди")

    def discuss_guests(self):
        while True:
            with self.lock:
                for table in self.tables:
                    if table.guest and not table.guest.is_alive():
                        print(f"{table.guest.name} покушал(-а) и ушёл(ушла)")
                        print(f"Стол номер {table.number} свободен")
                        table.guest = None
                    if table.guest is None and not self.q.empty():
                        next_guest = self.q.get()
                        table.guest = next_guest
                        print(
                            f"{next_guest.name} вышел(-ла) из очереди и сел(-а) за стол номер "
                            f"{table.number}"
                        )
                        next_guest.start()
            if self.q.empty() and all(table.guest is None for table in self.tables):
                break


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
    "Maria",
    "Oleg",
    "Vakhtang",
    "Sergey",
    "Darya",
    "Arman",
    "Vitoria",
    "Nikita",
    "Galina",
    "Pavel",
    "Ilya",
    "Alexandra",
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
