from threading import Thread
from random import randint
from time import sleep
from queue import Queue


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(Thread):
    def __init__(self, name_guest):
        self.name_guest = name_guest
        super().__init__()

    def run(self):
        sleep(randint(3, 10))


# Класс Cafe:
# Объекты этого класса должны создаваться следующим способом - Cafe(Table(1), Table(2),....)
# Обладать атрибутами queue - очередь (объект класса Queue) и tables - столы в этом кафе (любая коллекция).

class Cafe:
    def __init__(self, *tables):
        self.queue = Queue()
        self.tables = list(tables)
                                                 
    def guest_arrival(self, *guests):
        for guest in guests:
            for table in self.tables:
                if table.guest == None:
                    table.guest = guest
                    guest.start()
                    print(f"{guest.name_guest} сел(-а) за стол номер {table.number}")
                    break
            if not guest.is_alive():
                self.queue.put(guest)
                print(f"{guest.name_guest} в очереди")

    def discuss_guests(self):
        while not self.queue.empty() or self.busy_tables():
            busy_tables = [table for table in self.tables if table.guest != None]

            for table in busy_tables:
                if not table.guest.is_alive():
                    print(f"{table.guest.name_guest} за текущим столом> покушал(-а) и ушёл(ушла)")
                    table.guest = None
                    print(f"Стол номер {table.number} свободен")
                    if not self.queue.empty():
                        table.guest = self.queue.get()
                        table.guest.start()
                        print(f"{table.guest.name_guest} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")
            free_tables = [table for table in self.tables if table.guest == None]
            for table in free_tables:
                if not self.queue.empty():
                    table.guest = self.queue.get()
                    table.guest.start()
                    print(f"{table.guest.name_guest} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")

    def busy_tables(self):
        busy = False
        for table in self.tables:
            if not table.guest == None:
                busy = True
                break
        return busy


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
                'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra']
# Создание гостей
guests = [Guest(name) for name in guests_names]

# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
