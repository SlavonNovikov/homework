# Дополнительное практическое задание по модулю: "Наследование классов."
from math import sqrt, pi


class Figure:  # (родительский), Circle, Triangle и Cube
    sides_count = 0

    def __init__(self, color,sides):
        self.__sides = sides
        self.__color = list(color)
        self.filled = False

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if (0 <= r <= 255) and (0 <= g <= 255) and (0 <= b <= 255):
            return True
        return False

    def set_color(self,r,g,b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, new_sides):
        if len(new_sides) == self.sides_count:
            for side in new_sides:
                if side > 0:
                    return True
        return False

    def get_sides(self):
        return (self.__sides)

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(new_sides):
            self.__sides = list(new_sides)




class Circle(Figure):
    sides_count = 1

    def __init__(self, n_color=[], *n_sides):
        self.color = n_color
        if len(n_sides) != self.sides_count:
            self.sides = 1
        else:
            self.sides = n_sides[0]
        super().__init__(self.color, self.sides)

        self.__radius = self.sides / (2 * pi)

    def get_square(self):
        return self.sides ** 2 / (4 * pi)


class Triangle(Figure):
    sides_count = 3

    def __init__(self, n_color=[], *n_sides):
        self.color = n_color
        if len(n_sides) == 1:
            self.sides = list(n_sides) * self.sides_count
        elif len(n_sides) == self.sides_count:
            self.sides = list(n_sides)
        elif len(n_sides) != self.sides_count:
            self.sides = [1] * self.sides_count
        super().__init__(self.color, self.sides)

    def set_sides(self, *new_sides):
        if len(new_sides) == 1:
            self.sides = [new_sides] * 3
        elif len(new_sides) == self.sides_count:
            self.sides = list(new_sides)

    def get_sides(self):
        return self.sides

    def get_square(self):
        a = self.sides[0]
        b = self.sides[1]
        c = self.sides[2]
        p = 0.5*(a+b+c)
        return sqrt(p*(p-a)*(p-b)*(p-c))

class Cube(Figure):
    sides_count=12

    def __init__(self, n_color=[], *n_sides):
        self.color = n_color
        if len(n_sides) == 1:
            self.sides = list(n_sides) * self.sides_count
        elif len(n_sides) != self.sides_count:
            self.sides = [1] * self.sides_count
        super().__init__(self.color, self.sides)

    def get_volume(self):
        return (self.sides[0]**3)


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)

cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# # Проверка объёма (куба):
print(cube1.get_volume())

print("Еще одна проверка")
circle2 = Circle((200, 200, 100), 10, 15, 6)
print(circle2.get_sides())
print(circle1.get_sides())
print(circle1.get_square())
print(circle2.get_square())

print("Triangle")
Triangle1 = Triangle((200, 200, 200), 10, 6,9)
print(Triangle1.get_sides())
print(Triangle1.get_square())
cube2 = Cube((200, 200, 100), 9)
print(cube2.get_sides())
cube3 = Cube((200, 200, 100), 9, 12)
print(cube3.get_sides())
Triangle2 = Triangle((200, 200, 100), 4, 4, 6)
print(Triangle2.get_sides())
print(Triangle2.get_square())
print(len(Triangle2))