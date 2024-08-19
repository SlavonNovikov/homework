# Задача "Магические здания":
# Для решения этой задачи будем пользоваться решением к предыдущей задаче "Атрибуты и методы объекта".
#
# Необходимо дополнить класс House следующими специальными методами:
# __len__(self) - должен возвращать кол-во этажей здания self.number_of_floors.
# __str__(self) - должен возвращать строку: "Название: <название>, кол-во этажей: <этажи>".
#
# Пример результата выполнения программы:
# Пример выполняемого кода:
class House:
    def __init__(self, name, number_of_floor):
        self.name = name
        self.number_of_floor = number_of_floor
    def __str__(self):
        return f'Название:{self.name},кол-во этажей:{self.number_of_floor}'
    def __len__(self):
        return(self.number_of_floor)


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))




