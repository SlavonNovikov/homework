class House:
    def __init__(self, name, number_of_floor):
        self.name = name
        self.number_of_floor = number_of_floor

    def __str__(self):
        return f'Название:{self.name},кол-во этажей:{self.number_of_floor}'

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
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2)  # __eq__
h1 = h1 + 10  # __add__
print(h1)
print(h1 == h2)

h1 += 10  # __iadd__
print(h1)

h2 = 10 + h2  # __radd__
print(h2)

print(h1 > h2)  # __gt__
print(h1 >= h2)  # __ge__
print(h1 < h2)  # __lt__
print(h1 <= h2)  # __le__
print(h1 != h2)  # __ne__
