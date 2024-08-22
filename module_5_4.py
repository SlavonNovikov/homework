class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return object.__new__(cls)

    def __init__(self, name, number_of_floor):
        self.name = name
        self.number_of_floor = number_of_floor

    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")

    def go_to(self, new_floor):
        if new_floor > self.number_of_floor or new_floor < 1:
            print("Такого этажа не существует")
        else:
            for i in range(1, new_floor + 1):
                print(i)

    def __str__(self):
        return f'Название:{self.name},кол-во этажей:{self.number_of_floor}'

    def __len__(self):
        return (self.number_of_floor)

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floor == other.number_of_floor
        else:
            print ("Правый операнд должен быть типом House")

    def __add__(self, other):
        if isinstance(other, int):
            self.number_of_floor += other
        else:
            print("Правый операнд должен быть типом Int")
        return self

    def __iadd__(self, other):
        return self+other

    def __radd__(self, other):
        return self+other

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floor < other.number_of_floor
        else:
            print("Правый операнд должен быть типом House")


    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floor <= other.number_of_floor
        else:
            print("Правый операнд должен быть типом House")


    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floor > other.number_of_floor
        else:
            print("Правый операнд должен быть типом House")


    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floor >= other.number_of_floor
        else:
            print("Правый операнд должен быть типом House")


    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floor != other.number_of_floor
        else:
            print("Правый операнд должен быть типом House")




h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)
