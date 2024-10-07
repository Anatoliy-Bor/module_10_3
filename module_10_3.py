import threading
from random import randint
from time import sleep


class Bank:
    def __init__(self, balance=0):
        self.balance = int(balance)
        self.lock = threading.Lock()
    def deposit(self):
        #Будет совершать 100 транзакций пополнения средств.
        for i in range(100):
        #Пополнение - это увеличение баланса на случайное целое число от 50 до 500.
            refill = randint(50, 500)
            self.balance += refill
            print(f'Пополнение: {refill}. Баланс: {self.balance}.')
        #Если баланс больше или равен 500 и замок lock заблокирован - lock.locked()
            if self.balance >= 500 and self.lock.locked():
        #разблокировать его методом release
                self.lock.release()
            sleep(0.001)

    def take(self):
        #Будет совершать 100 транзакций снятия.
        for i in range(100):
        #Снятие - это уменьшение баланса на случайное целое число от 50 до 500.
            withdrawal = randint(50, 500)
            print(f'Запрос на {withdrawal}')
            if withdrawal <= self.balance:
                self.balance -= withdrawal
                print(f'Снятие: {withdrawal}. Баланс: {self.balance}.')
            else:
                print(f'Запрос отклонён, недостаточно средств')
                self.lock.acquire()
            # sleep(0.001)

bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')