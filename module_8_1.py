#Задание "Программистам всё можно":
# Реализуйте следующую функцию:
# add_everything_up, будет складывать числа(int, float) и строки(str)


def add_everything_up(a, b):
    s = ''
    try:
        s = a + b
    except TypeError:
        s = str(a) + str(b)
    return s

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))

# 123.456строка
# яблоко4215
# 130.456       