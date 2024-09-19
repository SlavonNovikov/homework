# Задача "Записать и запомнить":
# Создайте функцию custom_write(file_name, strings), которая принимает аргументы file_name - название файла для записи, strings - список строк для записи.
# Функция должна:
# Записывать в файл file_name все строки из списка strings, каждая на новой строке.
# Возвращать словарь strings_positions, где ключом будет кортеж (<номер строки>, <байт начала строки>), а значением - записываемая строка. Для получения номера байта начала строки используйте метод tell() перед записью.
# Пример полученного словаря:
# {(1, 0): 'Text for tell.', (2, 16): 'Используйте кодировку utf-8.'}
# Где:
# 1, 2 - номера записанных строк.
# 0, 16 - номера байт, на которых началась запись строк.
# 'Text for tell.', 'Используйте кодировку utf-8.' - сами строки.

# Вывод на консоль:
  # ((1, 0), 'Text for tell.')
  # ((2, 16), 'Используйте кодировку utf-8.')
  # ((3, 66), 'Because there are 2 languages!')
  # ((4, 98), 'Спасибо!')
  # Как выглядит файл после запуска:

def custom_write(file_name, string):
    file = open(file_name, 'w', encoding='utf-8')
    strings_positions = {}

    for i in range(len(string)):
        strings_positions[(i + 1, file.tell())] = string[i]
        file.write(string[i] + '\n')
    file.close()
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
