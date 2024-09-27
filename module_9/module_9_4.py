#"Создание функций на лету"

first = 'Мама мыла раму'
second = 'Рамена мало было'
my_func = lambda x, y: x == y
print(list(map(my_func, first, second)))


def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'w', encoding='utf8') as file:
            for i in range(len(data_set)):
                file.write(str(data_set[i]) + '\n')

    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'], 3, "4 строка")

from random import choice


class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return choice(self.words)


first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
