from os import system
system('clear')


# Встроенные функции Python — это функции, 
# которые уже включены в язык программирования и 
# доступны для использования без необходимости 
# дополнительного импорта библиотек. 

# Они обеспечивают простое и быстрое выполнение часто 
# используемых операций. 
# Рассмотрим основные категории и примеры встроенных функций.

# print() - Печатает содержимое объекта (Выводит)
# print('Hello world')

# len() - Возвращает длину объекта (Длина строки)
# print(len('Hello world'), len([1,2,4]))

# round() - Округляет число до указанного количества знаков
# print(round(3.141592, 2))

# enumerate() - возвращает элементы с их индексами.
# name = 'Marselle'
# for i, letter in enumerate(name, start=0):
#     print(i, letter)

# abs() - возвращает модуль числа.
# print(abs(-5), abs(5))

# pow(x, y) - возводит число x в степень y (эквивалентно x**y).
# print(pow(10, 2))

# max() - возвращает максимальный элемент массива.
# print(max((1, 2, 3, 434, 2344)))
# print(max([1, 2, 3, 434, 2344]))
# print(max({1, 2, 3, 434, 2344}))

# min() - возвращает минимальный элемент массива.
# print(min((1, 2, 3, 434, 2344)))
# print(min([1, 2, 3, 434, 2344]))
# print(min({1, 2, 3, 434, 2344}))

# sum() - суммирует все элементы последовательности.
# print(sum({1, 2, 3, 434, 2344}))
# print(sum([1, 2, 3, 434, 2344]))
# print(sum((1, 2, 3, 434, 2344)))

# str() - неизменяются
# print(str(123))
# print(str({'n': 1}))
# print(str([1,2,3,4]))
# print(str(True))

# int() - неизменяются
# float() - неизменяются
# bool() - неизменяются
# tuple() - неизменяются
# print(tuple([1,2,3]))
# print(tuple({1,2,3}))
# print(tuple('1,2,3'))

# frozenset() - неизменяются
# print(frozenset([1, 3, 2, 1]))

# list() - изменяются
# dict() - изменяются
# print(dict(name='marselle', age=12))

# set() - изменяются

# input() - позволяет пользователю вводить данные с клавиатуры.
# print(input('Введите что-то: '))

# ord() - преобразуют символ в код Unicode.
# print(ord('9'))

# chr() - преобразуют код Unicode в символ.
# print(chr(109))

# type() - возвращает тип объекта.
# a = list('m')
# print(type(a))

# isinstance() - проверяет, относится ли объект к указанному типу.
# print(isinstance(1, str))

# range(start, stop, step) - создает последовательность чисел.
# print(list(range(1, 10, 2)))
# print(set(range(10)))
# print(tuple(range(1, 10)))
# for i in range(1, 10, 2):
#     print(i)

# zip() - объединяет элементы из нескольких последовательностей в кортежи.
# print(dict(zip([1, 2, 3], ['a', 'b', 'c'])))
# print({1: 'a', 2: 'b', 3: 'c'}.items())

# a = ['marselle', '123', 3]
# b = ('1', 2, 3)

# # print(dict(zip(a, b)))

# for k, v in zip(a, b):
#     print(k, v)


# sorted() - сортирует последовательность.
# print(sorted((1, 3, 2, 4, 5, 6, 7, 8, 9, 10), reverse=True))
# print(sorted(['a', 'c', 'b']))

# dir() - возвращает список атрибутов объекта.
# print(dir(list()))
# print(dir(tuple()))
# print(dir(set()))
# print(dir(int()))


# List comprehension (или списковое включение) — это синтаксический 
# сахар в Python, который позволяет создавать новые списки из 
# других коллекций с использованием 
# более компактного и читаемого синтаксиса.

# [выражение for элемент in коллекция if условие]

# выражение — операция, выполняемая над каждым элементом.
# for элемент in коллекция — цикл, проходящий по всем элементам коллекции.
# if условие (необязательно) — фильтрация элементов по условию.



# n = list(range(1, 11))
# even = []
# print(n)

# for i in n:
#     if i % 2 == 0:
#         even.append(i)

# print(even)
# print()

# print([i for i in range(1, 11) if i % 2 == 0])

# name = ''

# print(name if name else 'No name')

# a = 'No name' if not name else name
# print(a)

# a = ''
# if not name:
#     a = 'No name'
# else:
#     a = name

# print(a)


# print([i**2 for i in range(1, 11)])
# print([i+1 for i in range(1, 11)])
# print([i+i for i in range(1, 11) if i % 2 == 0])


# words = ["apple", "banana", "cherry"]

# lengths = [len(i) for i in words]
# print(lengths) 

# users = {
#     'ItcBootcamp': 'iloveITC',
#     'anton': '234',
#     'aliya': '345',
#     'jaks': '456',
# }

# print({k: v for k, v in users.items() if '4' in v})


# for i in [12.2123, 234.23123, 'asd']:
#     if isinstance(i, float):
#         print(round(i, 2))
#     else:
#         print(i)


# print(max([12.2123, 234.23123], ))


# 4. Функции `max()` и `min()`.  
#    Напишите программу, которая принимает от пользователя список чисел 
# (в одну строку через пробел) и выводит максимальное и минимальное 
# число из этого списка.


# input('Введите числа через пробел: ').split()

# numbers = input('Введите числа через пробел: ').split()

# print(
#     f"max: {max([int(i) for i in numbers])}",
#     f"min: {min([int(i) for i in numbers])}",
# )

# numbers = [int(i) for i in input("Введите числа через пробел: ").split()]
# print(f"{sum(numbers)}")

# 6. Проверка типа данных с помощью `isinstance()` и `type()`.  
#    Напишите программу, которая принимает ввод от пользователя и проверяет, 
# является ли введенное значение строкой. Выведите результат проверки.

a = input('Введите что-то: ')
for i in a:
    if isinstance(a, str):
        print('Строка')
        print(type(a))