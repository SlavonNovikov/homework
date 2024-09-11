from math import sqrt, pi


class Figure():
    sides_count = 0

    def __init__(self,__color = [], __sides = []):
        self.__color = __color
        self.__sides = __sides
        self.filled = False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
        else:
            self.__color = list(self.color)
    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if (0 <= r <= 255) and (0 <= g <= 255) and (0 <= b <= 255):
            return True
        return False

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(new_sides):
            self.__sides = list(new_sides)

    def get_sides(self):
        return self.__sides

    def __is_valid_sides(self, new_sides):
        if len(new_sides) == self.sides_count:
            for side in new_sides:
                if side > 0:
                    return True
        return False


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        self.color = color
        #self.sides = [sides]
        self.__color = [color]
        if len(sides) != 1:
            sides = 1
        else:
            sides = sides[0]
        self.__sides = [sides]
        super().__init__(self)
        self.sides = [sides]

    def get_square(self):
        self.__radius = self.sides[0]/(2*pi)
        return pi * self.__radius ** 2


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        self.color = color
        self.sides = sides
        self.__color = [color]
        if len(sides) != 3:
            sides = 1
        else:
            sides = sides[0]
        self.__sides = [sides]
        super().__init__(self)
        self.sides = [sides]*3

    def set_sides(self, *new_sides):
        if len(new_sides) == 1:
            self.sides = [new_sides]*3
        elif len(new_sides) == self.sides_count:
            self.sides = list(new_sides)

    def get_sides(self):
        return self.sides

    def get_square(self):
        a = self.sides[0]
        b = self.sides[1]
        c = self.sides[2]
        p = (a + b + c) / 2
        S = sqrt(p*(p - a)+(p - b)+(p - c)),
        return S


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        self.color = color
        self.sides = sides
        self.__color = [color]
        if len(sides) != 1:
            sides = 1
        else:
            sides = sides[0]
        self.__sides = [sides]
        super().__init__(self)
        self.sides = [sides]*12

    def set_sides(self, *new_sides):
        if len(new_sides) == 1:
            self.sides = [new_sides]*12
        elif len(new_sides) == self.sides_count:
            self.sides = list(new_sides)

    def get_sides(self):
        return self.sides
    def get_volume(self):
        return self.sides[0] ** 3


circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
