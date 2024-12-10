# 1. Проверка числа на положительность
#    - Попросите пользователя ввести целое число. Напишите программу, которая проверяет, является ли число положительным.
#    - Пример:  
#      Введите число: -5  
#      Вывод: Число отрицательное.

# chislo = int(input("Введите число: "))
# print(chislo >= 0 and "Число положительное" or "Число отрицательное")

# number = int(input("Enter an integer: "))     
# result = (number > 0) * "The number is positive." or (number < 0) * "The number is negative." or "The number is zero."
# print(result)


# print(int(input("Введите число: ")) >= 0 or "Число отрицательное" )


# a = int(input('Введите число:'))
# print(a < 0 and 'Число отрицательное.')

# 2. Преобразование из `int` в `str`
#    - Попросите пользователя ввести число, преобразуйте его в строку и выведите результат вместе с типом данных.
#    - Пример:  
#      Введите число: 100  
#      Вывод: 100, тип данных <class 'str'>.


    # number = int(input("Enter an number: "))
    # number = str(number)
    # print(f'Output: {number}, data type: {type(number)}')



# 3. Конвертер километров в метры
#    - Напишите программу, которая принимает расстояние в километрах и переводит его в метры. (1 км = 1000 метров)
#    - Пример:  
#      Введите расстояние в километрах: 5  
#      Вывод: 5000 метров.


# kilometers = int(input("Enter the distance in kilometers: "))
# meters = kilometers * 1000
# print(f'Output: {meters} meters.')



# 4. Калькулятор деления с остатком
#    - Попросите пользователя ввести два числа, затем напишите программу, которая показывает результат целочисленного деления и остаток.
#    - Пример:  
#      Введите первое число: 10  
#      Введите второе число: 3  
#      Вывод: Частное = 3, Остаток = 1.



# number_1 = int(input("Enter the first number: "))
# number_2 = int(input("Enter the second number: "))
# quotient = number_1 // number_2
# remainder = number_1 % number_2
# print(f'Output: Quotient = {quotient}, remainder = {remainder}.')


# 5. Создание приветственного сообщения
#    - Напишите программу, которая запрашивает у пользователя его имя и возраст, а затем выводит сообщение с приветствием и информацией о возрасте.
#    - Пример:  
#      Введите ваше имя: Анна  
#      Введите ваш возраст: 25  
#      Вывод: Привет, Анна! Вам 25 лет.


# name = input('Enter your name: ')
# name = name.capitalize()
# age = input(f"{name}, Enter your age: ")
# print(f'Hello, {name}, your age is {age} years old!')



# 6. Чётное или нечётное число
#    - Попросите пользователя ввести целое число и определите, является ли оно чётным или нечётным, как в примере кода.
#    - Пример:  
#      Введите число: 7  
#      Вывод: Нечётное.


# number = int(input("Enter a number: "))
# result = (number % 2 == 0) * 'The number is even.' or 'The number os odd.'
# print(result)



# 7. Расчёт площади прямоугольника
#    - Запросите у пользователя длину и ширину прямоугольника и посчитайте его площадь.
#    - Пример:  
#      Введите длину: 8  
#      Введите ширину: 4  
#      Вывод: Площадь прямоугольника: 32.


# length_of_triangle = int(input("Enter length of triangle: "))
# width_of_triangle = int(input("Enter wight of triangle: "))
# area_of_triangle = length_of_triangle * width_of_triangle
# print(f'Area of triangle is {area_of_triangle}.')



# 8. Температурный конвертер
#    - Напишите программу, которая переводит температуру из градусов Цельсия в Фаренгейты.
#    - Пример:  
#      Введите температуру в Цельсиях: 0  
#      Вывод: Температура в Фаренгейтах: 32.



# degree_celsius = int(input("Enter degree in Celsius: "))
# degree_fahrengeit = degree_celsius * 9/5 + 32
# print(f'Temperature in Fahrenheit: {degree_fahrengeit}')




# 9. Конвертер секунд
#    - Запросите у пользователя количество секунд и преобразуйте его в часы, минуты и секунды.
#    - Пример:  
#      Введите количество секунд: 3665  
#      Вывод: 1 час 1 минута 5 секунд.



# seconds = int(input("Enter number of seconds: "))
# seconds_amount = seconds % 60
# minutes_amount = (seconds % 3600) // 60
# hours_amount = seconds // 3600
# print(f'{hours_amount} hour(s), {minutes_amount} minute(s), {seconds_amount} second(s)')


# 10. Калькулятор разности годов
#     - Напишите программу, которая принимает два года и выводит разницу между ними.
#     - Пример:  
#       Введите год рождения: 1990  
#       Введите текущий год: 2024  
#       Вывод: Разница 34 года.



# birth_year = int(input('Enter the birth year: '))
# current_year = int(input('Enter the current year: '))
# difference = abs(current_year - birth_year)
# print(f'The difference is {difference}')
