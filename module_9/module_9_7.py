#Декораторы

# Напишите 2 функции:
# Функция, которая складывает 3 числа (sum_three)
# Функция декоратор (is_prime), которая распечатывает "Простое", если результат 1ой функции будет простым числом и "Составное" в противном случае.

def is_prime(func):
    def wrapper(*args):
        result= func(*args)
        if result > 1:
            simple = True
            for divider in range(2, result):
                if result % divider == 0:
                    simple = False
                    break
            if simple:
                print('Простое')
            else:
                print('Составное')

        return result
    return wrapper


@is_prime
def sum_three(*args):
    return sum(args)


result = sum_three(1, 1, 5,6)
print(result)
