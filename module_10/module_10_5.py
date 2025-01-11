from datetime import datetime
import multiprocessing


def read_info(name):
    with open(name, 'r') as file:
        all_data = [line for line in file]


filenames = [f'./file {number}.txt' for number in range(1, 5)]

# Линейный вызов
# time_start = datetime.now()
# for file in filenames:
#     read_info(file)
# time_end = datetime.now()
# time_result = time_end - time_start
# print(f'Время считывания файлов при линейном вызове-{time_result}')

# Многопроцессный
if __name__ == '__main__':
    time_start = datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, filenames)
    time_end = datetime.now()
    time_result = time_end - time_start
    print(f'Время считывания файлов при мультипроцессном вызове-{time_result}')
