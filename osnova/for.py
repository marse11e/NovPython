from os import system
system('clear')


# for переменная in последовательность:
    # блок кода, выполняемый на каждой итерации

# names = ['Ali', 'Vladimir', 'Marselle', 'Raf']

# for name in names:
#     if 'Marselle' == name:
#         print(f'Hello, {name}')
#     else:
#         print(name)

# fruits = ["яблоко", "груша", "банан"]

# for fruit in fruits:
#     print(fruit)


# LIST, SET and TUPLE
# START, STOP, STEP
# numbers = tuple(range(1, 11))
# print(numbers)

# res = 0
# for num in numbers:
#     res += num
#     # print('iter', num)

# print( 'temp_sum', res)



# names = ['Ali', 'Vladimir', 10, 'Marselle', 'Raf']

# for name in names:
#     print(name)

#     if type(name) == str:
#         for char in name:
#             print(char)

# name = 'Vladimir'

# for char in name:
#     print(char)


# languages = ['Python', 'C++', 'C#', 'C', 'Java', 'JavaScript']
#             # [0, 1, 2, 3, 4, 5]
# for index, lan in enumerate(languages, start=0):
#     print(index, lan)



# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even = []
# odd = []

# for num in numbers:
#     if num == 0:
#         continue

#     if num % 2 == 0:
#         even.append(num)
#     else:
#         odd.append(num)

# print('Четные числа:', even)
# print('Нечетные числа:', odd)



num = [0, 1, 2, 3, 4, 5]

print(max(num))
print(min(num))

print(any(num))
print(all(num))

print(sum(num))




numbers = [2, 4, 6, 8, 10]
print(sum(numbers))  # Результат: 30

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
print(even_numbers)  # Результат: [2, 4, 6, 8, 10]



n = int(input('Введите число: '))
print(sum(range(1, n + 1)))


for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")


words = ["apple", "banana", "cherry", "date"]

for i in words:
    print(len(i))



vowels = "aeiou"
text = "programming is fun"
vowel_count = 0
for char in text.lower():
    if char in vowels:
        vowel_count += 1

print(vowel_count)