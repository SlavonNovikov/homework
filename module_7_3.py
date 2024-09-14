# Задача "Найдёт везде":
# Напишите класс WordsFinder, объекты которого создаются следующим образом:
# WordsFinder('file1.txt, file2.txt', 'file3.txt', ...).
# Объект этого класса должен принимать при создании неограниченного количество названий файлов и записывать их в атрибут file_names в виде списка или кортежа.
#
# Также объект класса WordsFinder должен обладать следующими методами:
# get_all_words - подготовительный метод, который возвращает словарь следующего вида:
# {'file1.txt': ['word1', 'word2'], 'file2.txt': ['word3', 'word4'], 'file3.txt': ['word5', 'word6', 'word7']}
# Где:
# 'file1.txt', 'file2.txt', ''file3.txt'' - названия файлов.
# ['word1', 'word2'], ['word3', 'word4'], ['word5', 'word6', 'word7'] - слова содержащиеся в этом файле.
# Алгоритм получения словаря такого вида в методе get_all_words:
# Создайте пустой словарь all_words.
# Переберите названия файлов и открывайте каждый из них, используя оператор with.
# Для каждого файла считывайте единые строки, переводя их в нижний регистр (метод lower()).
# Избавьтесь от пунктуации [',', '.', '=', '!', '?', ';', ':', ' - '] в строке. (тире обособлено пробелами, это не дефис в слове).
# Разбейте эту строку на элементы списка методом split(). (разбивается по умолчанию по пробелу)
# В словарь all_words запишите полученные данные, ключ - название файла, значение - список из слов этого файла.



class WordsFinder:
    def __init__(self,*name):
        self.file_names = list(name)

    def get_all_words(self):
        all_words = {}
        str_word = ''
        for i in self.file_names:
            with open(i, encoding = 'utf-8') as file:
                for j in file:
                    str_word +=' '.join(j.split())
        for char in str_word:
            if char in [',','?','!','.','\n','=',':',';',' - ']:
                str_word = str_word.replace(char,' ')

        str_word = str_word.lower()
        str_word = str_word.split()
        all_words = {i: str_word }
        return all_words

    def find(self, word):
        index_words = {}
        str_word = self.get_all_words()
        for i,j in str_word.items():
            index = j.index(word.lower())+1
            break
        index_words = {i: index}
        return index_words

    def count(self, word):
        count_words = {}
        count_word = 0
        str_word = self.get_all_words()
        for i, j in str_word.items():
            count_word += j.count(word.lower())
            break
        count_words = {i: count_word}
        return count_words



finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))
