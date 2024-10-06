#"Блокировки и обработка ошибок"

from threading import Thread, Lock
import random
from time import sleep

lock=Lock()

class Bank:
    def __init__(self,balance=0):
        self.balance=balance
        self.lock=Lock()


    def deposit(self):
        for i in range(100):
            cash_deposit = random.randint(50, 500)
            self.balance += cash_deposit
            if self.balance>=500 and lock.locked():
                lock.release()
            print(f'Пополнение:{cash_deposit}. Баланс: {self.balance}')
            sleep(0.001)
        return self.balance

    def take(self):
        for i in range(100):
            cash_withdrawal=random.randint(50,500)
            print(f'Запрос на {cash_withdrawal}.')
            if cash_withdrawal<=self.balance:
                self.balance -= cash_withdrawal
                print(f'Снятие:{cash_withdrawal}.Баланс:{self.balance}')
            else:
                print('Запрос отклонён, недостаточно средств')
                lock.acquire()
            sleep(0.001)
        return self.balance

bk = Bank()

th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
