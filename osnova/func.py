from os import system
system('clear')


# def num_sum(a, y):
#     return a + y

# r = num_sum(10, 5)
# print(r)

# def generated(n):
#     a = []
#     for i in range(n+1):
#         a.append(i)
#         if i == 5:
#             return a

# print(generated(3))

# def custom_print(a, b):
#     """
#     Это функция custom_print
#     Параметры:
#         a: Any
#         b: Any
    
#     функция ничего не возвращает она из ветки и палок
#     """
#     print("1 " + a)

# custom_print("12", 12)

# Сложение двух чисел
# Напишите функцию, которая принимает два числа и возвращает их сумму.
# def add_numbers(x, y):
#     return x + y

# print(add_numbers(10, 30))


# Проверка четности числа
# Напишите функцию, которая принимает число и возвращает True, 
# если оно четное, и False в противном случае.
# def is_even(x: int) -> bool:
#     """
#     Функцию, которая принимает число и возвращает True, если оно четное, и False в противном случае.
#     """
#     return x % 2 == 0

# print(is_even(1))


# Максимум из трёх чисел
# Напишите функцию, которая принимает три числа 
# и возвращает наибольшее из них.
# def max_of_three(a, b, c):
#     return max([a, b, c])

# print(max_of_three(1, 2, 3))


# Реверс строки
# Напишите функцию, которая принимает строку и 
# возвращает её в обратном порядке.
# def reverse_string(s):
#     return s[::-1]

# print(reverse_string('Marselle'))
# print(reverse_string('123123'))
# print(reverse_string('qweqwe'))
# print(reverse_string('asdasd'))

# Сумма чисел списка
# Напишите функцию, которая принимает список 
# чисел и возвращает их сумму.
def sum_list(numbers):
    return sum(numbers)

print(sum_list([1, 2, 3, 4, 5]))

# Поиск индекса элемента в списке
# Напишите функцию, которая принимает список и элемент, 
# а затем возвращает индекс элемента (или -1, если элемента нет).
def find_index(lst, value):
    try:
        return lst.index(value)
    except ValueError:
        return -1
    
# Нахождение среднего значения
# Напишите функцию, которая принимает список чисел 
# и возвращает их среднее значение.
def average(numbers):
    if numbers:
        return sum(numbers) / len(numbers)
    return 0

print(average([1, 2, 3, 4, 5]))

# def average(numbers):
#     return sum(numbers) / len(numbers) if numbers else 0
    
# Удаление дубликатов из списка
# Напишите функцию, которая принимает список и 
# возвращает новый список без дубликатов.
def remove_duplicates(lst):
    return list(set(lst))
    
# Подсчёт гласных в строке
# Напишите функцию, которая принимает строку и возвращает количество гласных букв в ней.
def count_vowels(s):
    return sum(1 for char in s if char in 'aeiouAEIOU')



