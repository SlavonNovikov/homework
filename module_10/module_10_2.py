#Потоки на классах"

from threading import Thread
from time import sleep

class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power


    def run(self):
        print(f'{self.name}, на нас напали!')
        warrior = 100
        day = 0

        while warrior > 0:
            warrior -= self.power
            if warrior < 0:
                warrior = 0
            day += 1
            print(f'{self.name} сражается {day} день(дня), осталось {warrior} воинов.')
            sleep(1)
        print(f'{self.name} одержал победу спустя {day} дней(дня)!')




# Создание класса
first_knight = Knight('Sir Lancelot', 9)
second_knight = Knight("Sir Galahad", 20)


first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print('Все битвы закончились!')

