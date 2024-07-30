# 1.Функция с параметрами по умолчанию:
# Создайте функцию print_params(a = 1, b = 'строка', c = True), которая принимает три параметра со
# значениями по умолчанию (например сейчас это: 1, 'строка', True).
# Функция должна выводить эти параметры.
# Вызовите функцию print_params с разным количеством аргументов, включая вызов без аргументов.
# Проверьте, работают ли вызовы print_params(b = 25) print_params(c = [1,2,3])
def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params()
print_params(b=25)
print_params(a=2, c=5)
print_params(c=[1, 2, 3])

# Создайте список values_list с тремя элементами разных типов.
# Создайте словарь values_dict с тремя ключами, соответствующими параметрам функции print_params,
# и значениями разных типов.
# Передайте values_list и values_dict в функцию print_params, используя распаковку параметров
# (* для списка и ** для словаря).

values_list = [55, 'много строк', False]
values_dict = {"a": 11, "b": "множество", "c": False}
print_params(*values_list)  # распаковка списка values_list
print_params(**values_dict)  # распаковка словаря values_dict


# 3.Распаковка + отдельные параметры:
# Создайте список values_list_2 с двумя элементами разных типов
# Проверьте, работает ли print_params(*values_list_2, 42)

values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)