from os import system
system('clear')


# datetime — это модуль Python, который предоставляет классы для работы с датами 
# и временем. Он поддерживает вычисления с датами, форматирование, 
# сравнение и извлечение компонентов времени.


# import datetime

# from datetime import datetime

# Созданные модули
# import test
# from test import a, b, name, surname
# from test import *

# from test import name as n, surname as s


# print(a)
# print(b)
# print(n)
# print(s)

# print(test.a)
# print(test.b)
# print(test.name)
# print(test.surname)


# Встроенные модули (библиотека)
# import datetime

# # Скачанные модули (библиотека)
# pass


# from datetime import datetime, date, time, tzinfo, timezone

# Основные классы модуля datetime:
#     datetime.date: Представляет дату (год, месяц, день).

#     datetime.time: Представляет время (часы, минуты, секунды, микросекунды).

#     datetime.datetime: Содержит дату и время.

#     datetime.timedelta: Представляет разницу между двумя объектами даты или времени.

#     datetime.tzinfo: Базовый класс для поддержки часовых поясов.

#     datetime.timezone: Конкретная реализация часовых поясов.


# today = datetime.today()
# print("Сегодняшняя дата:", today)

# custom_date = date(1976, 5, 13)
# # print(custom_date)

# custom_time = time(12, 30, 45, 12)
# # print(custom_time)

# print(custom_date.day)
# print(custom_date.month)
# print(custom_date.year)
# print(custom_time.hour)
# print(custom_time.minute)
# print(custom_time.second)
# print(custom_time.microsecond)
# print(today.weekday())


# # Текущая дата
# today = date.today()
# print("Сегодняшняя дата:", today)

# # Создание конкретной даты
# custom_date = date(2024, 11, 30)
# print("Созданная дата:", custom_date)

# # Извлечение компонентов даты
# print("Год:", today.year)
# print("Месяц:", today.month)
# print("День:", today.day)


# # Создание времени
# custom_time = time(14, 30, 45)
# print("Время:", custom_time)

# # Извлечение компонентов времени
# print("Часы:", custom_time.hour)
# print("Минуты:", custom_time.minute)
# print("Секунды:", custom_time.second)


# Текущая дата и время
# now = datetime.now()
# print("Текущая дата и время:", now)

# # Создание конкретного datetime
# custom_datetime = datetime(2024, 11, 27, 14, 30, 45, 123456)
# print("Созданный datetime:", custom_datetime)

# # Извлечение компонентов datetime
# print("Год:", now.year)
# print("Месяц:", now.month)
# print("День:", now.day)
# print("Часы:", now.hour)
# print("Минуты:", now.minute)
# print("Секунды:", now.second)
# print("Микросекунды:", now.microsecond)



# # Разница между двумя датами
# data1 = datetime(2024, 11, 27)
# data2 = datetime(2024, 11, 30, 14, 30, 45)

# delta = data2 - data1
# print("Разница:", delta)

# now = datetime.now()
# print("Сейчас:", now)

# tomorrow = now + timedelta(days=True, hours=-3)
# print("Завтра:", tomorrow)

# yesterday = now - timedelta(days=1)
# print("Вчера:", yesterday)


# now = datetime.now().strftime("%d - %B / %y %H:%M %A ")
# print("Сейчас:", now)

# datetime_str = '2000-11. 11 14:30:12'
# datetime_obj = datetime.strptime(datetime_str, '%Y-%m. %d %H:%M:%S')
# print(datetime_obj)


# import random

# random — это встроенный модуль Python, предоставляющий 
# функции для генерации случайных чисел, случайного выбора 
# элементов и выполнения других операций, связанных со случайностью.


# [
#     'seed', 'random','randint', 
#     'choice', 'randrange', 'sample', 
#     'shuffle', 'choices'
# ]

# from random import ( 
#     randint, seed, choice, 
#     choices, shuffle, random,
#     randrange, sample
# )

# Возвращает случайное число диапазоне [a, b].
# print(randint(1000000, 9999999))

# Возвращает случайное число с плавающей запятой в диапазоне [0.0, 1.0].
# print(random())


# my_loto = list(range(1, 8))
# # Перемешивает последовательность на месте.
# shuffle(my_loto)
# print(my_loto)


# print(choice(my_loto))
# print(choices(my_loto, k=3))

# # import random
# # random.seed(34)
# # print(random.random())

# # print(randrange(20, 40, 2))

# my_loto = list(range(1, 8))

# print(sample(my_loto, k=3))



# from random import choices

# my_loto = list(range(1, 8))
# print(my_loto)
# print(choices(my_loto, k=3))



# a = list(range(1,8))

# p = 0
# t = ''
# while 'Выигрышь' not in t:
#     i = choices(a, k=3)
#     print(i)


#     if i[0] == 1 and i[1] == 1 and i[2] == 1:
#         t = 'Выигрышь'
#         print('Выигрышь 100 тг')
#     elif i[0] == 2 and i[1] == 2 and i[2] == 2:
#         t = 'Выигрышь'

#         print('Выигрышь 200 тг')
#     elif i[0] == 3 and i[1] == 3 and i[2] == 3:
#         t = 'Выигрышь'

#         print('Выигрышь 300 тг')
#     elif i[0] == 4 and i[1] == 4 and i[2] == 4:
#         t = 'Выигрышь'

#         print('Выигрышь 400 тг')
#     elif i[0] == 5 and i[1] == 5 and i[2] == 5:
#         t = 'Выигрышь'

#         print('Выигрышь 500 тг')
#     elif i[0] == 6 and i[1] == 6 and i[2] == 6:
#         t = 'Выигрышь'

#         print('Выигрышь 600 тг')
#     elif i[0] == 7 and i[1] == 7 and i[2] == 7:
#         t = 'Выигрышь'

#         print('Выигрышь 1000000 тг')
#     else:
#         p += 1
#         print('Вы проиграли!')
# else:
#     print(f'Проиграли {p*100} тг', 'Кол проиг:', p)

# from random import choices

# win = 0
# profit = 0
# your_try = 1
# while True:
#     numbers = list(range(1, 8))
#     result = choices(numbers, k=3)
#     print('Ваши числа:', result)
#     if result[0] == result[1] == result[2]:
#         if 7 in result:
#             if win <= 5:
#                 win += 1
#                 continue
#             else:
#                 print(f'Выигрышь 1 000 000 тг | Потрачено {profit} тг')
#                 break
#         else:
#             if win <= 3:
#                 win += 1
#                 continue
#             else:
#                 print(f'Выигрышь 1000 тг | Потрачено {profit} тг')
#                 break
#     else:
#         your_try += 1
#         profit = your_try * 10
#         print(f'Вы проиграли {your_try} раз')


# from os import (
#     getcwd, path, mkdir, 
#     makedirs, remove, rmdir, 
#     removedirs, rename, system, 
#     getpid, getppid
# )

# # Возвращает текущую рабочую директорию (каталог).
# current_directory = getcwd()
# print("Текущая рабочая директория:", current_directory)

# # Правильное соединение частей пути в одну строку. 
# path_ = path.join('A', 'B.txt', 'C.txt')
# custom_path = '/'.join(['A', 'B.txt', 'C.txt'])
# print("Полный путь:", path)
# print("Полный путь:", custom_path)

# # Проверяет, существует ли путь (файл или директория).
# exists_folder = path.exists('/home/marselle/NovPython')
# exists_file = path.exists('/home/marselle/NovPython/modules.py')
# print("Folder существует:", exists_folder)
# print("File существует:", exists_file)

# Создает директорию по указанному пути.
# mkdir('1')
# mkdir('2')
# mkdir('3')

# Создает все промежуточные директории, если они не существуют.
# makedirs('1/2/3/4/5/6/7/8/9/10')

# Удаляет файл.
# remove('config.ini')

# Удаляет пустую директорию.
# rmdir('1')

# Удаляет директорию и все пустые родительские директории.
# removedirs('1/2/3/4/5/6/7/8/9/10')

# Переименовывает файл или директорию с пути src в путь dst.
# rename('3', 'core')

# Выполняет команду в командной строке или терминале и 
# возвращает ее код завершения.
# system('echo Hello, Aigulya!')

# # Возвращает ID текущего процесса.
# print(getpid())

# # Возвращает ID родительского процесса.
# print(getppid())


# system('mkdir -p 1/2/3')
# system('touch 1')

from sys import (
    maxsize, executable, version, platform
)

print("Максимальный размер числа:", maxsize)
print("Путь к Python:", executable)
print("Версия Python:", version)
print("Операционная система:", platform)