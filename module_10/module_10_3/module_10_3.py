from random import randint
from threading import Lock, Thread
from time import sleep


class Bank(Thread):
    def __init__(self):
        super().__init__()
        self.balance: int = 0
        self.lock = Lock()
        self.print_lock = Lock()

    def deposit(self):
        transaction_plus = 0
        while transaction_plus < 100:
            num = randint(50, 500)
            self.lock.acquire()
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            self.balance += num
            with self.print_lock:
                print(f"Пополнение: {num}. Баланс: {self.balance}")
            sleep(0.001)
            transaction_plus += 1
            if self.lock.locked():
                self.lock.release()

    def take(self):
        transaction_minus = 0
        while transaction_minus < 100:
            num = randint(50, 500)
            with self.print_lock:
                print(f"Запрос на {num}")
            self.lock.acquire()
            if num <= self.balance:
                self.balance -= num
                with self.print_lock:
                    print(f"Снятие: {num}. Баланс: {self.balance}")
                if self.lock.locked():
                    self.lock.release()
            else:
                with self.print_lock:
                    print("Запрос отклонён, недостаточно средств")
                if not self.lock.locked():
                    self.lock.acquire()
            if self.lock.locked():
                self.lock.release()
            sleep(0.001)
            transaction_minus += 1


bk = Bank()
th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()

th1.join()
th2.join()

print(f"Итоговый баланс: {bk.balance}")
