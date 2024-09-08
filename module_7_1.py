# Задача "Учёт товаров":
from pprint import pprint
class Product: #Product('Potato', 50.0, 'Vagetables')

    def __init__(self,name,weight,category):
        self.name=name
        self.weight=weight
        self.category=category

    # Метод __str__, возвращает строку в формате '<название>, <вес>, <категория>'.Все
    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

# Метод get_products(self), который считывает всю информацию из файла __file_name,
# закрывает его и возвращает единую строку со всеми товарами из файла __file_name.
# Метод add(self, *products), который принимает неограниченное количество объектов
# класса Product. Добавляет в файл __file_name каждый продукт из products,
# если его ещё нет в файле (по названию). Если такой продукт уже есть, то не добавляет
# и выводит строку 'Продукт <название> уже есть в магазине' .

class Shop():
    def __init__(self):
        self.__file_name = 'products.txt'
        self.product_list = []

    def get_products(self):
        file = open(self.__file_name, 'r')
        self.product_list = file.read()
        file.close()
        return self.product_list

    def add(self, *new_products):
        s1.get_products()
        file = open(self.__file_name, 'a')
        for temp_product in new_products:
            if Product.__str__(temp_product) in self.product_list:
                print(f'Товар {temp_product.name} уже есть в магазине')
            else:
                file.write(Product.__str__(temp_product) + '\n')
        file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
p1 = Product('Potato', 50.5, 'Vegetables')
print(p1)
print(p2) # __str__
s1.add(p1, p2, p3)

print(s1.get_products())
