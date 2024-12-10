from os import system
system('clear')



# Работа с файлами в Python включает в себя открытие, чтение, запись и закрытие файлов. 
# Вы можете использовать функцию open() для открытия файла, указать режим 
# (чтение, запись, добавление) и затем использовать методы, такие как read(), write(), 
# и другие для взаимодействия с содержимым файла. Не забывайте закрывать файл с 
# помощью close(), чтобы освободить ресурсы.


# file = open('имя_файла', 'режим')
# file.close()

# file = open('file.txt', 'w')
# # file.write('Hello, World!')
# file.write('Hello!')
# file.close()


# file2 = open('file1.txt', 'a')
# file2.write('Hello, World!')
# file2.close()

# file3 = open('file.txt', 'r')
# text = file3.read()
# print(text)
# file3.close()

# Функция open() в Python используется для открытия файлов. 
# Ее синтаксис выглядит следующим образом:
# file = open('имя_файла', 'режим')

# Где:
# - 'имя_файла' - это строка, содержащая имя или путь к файлу.
# - 'режим' - это строка, указывающая режим открытия файла:
#   - 'r': чтение (по умолчанию).
#   - 'w': запись (существующий файл будет очищен, если файл не существует, 
#         он будет создан).
#   - 'a': добавление (добавление данных в конец файла).


# example = open('example.txt', 'r')
# text = example.read()
# text = example.read(51)
# text = example.readline()
# text = example.readlines(128)
# print(text)
# example.close()

# Обработка исключений при работе с файлами:
# FileNotFoundError — Файл не найден.
# PermissionError — Нет доступа к файлу.
# IsADirectoryError — Пытались открыть каталог как файл.


# file = open('file.txt', 'w')
# file.write("Это новая строка текста.\n")
# file.close()

# file2 = open('file.txt', 'a')
# file2.write("Эта строка добавлена.\n")
# file2.close()

# file = open('file.txt', 'w')
# file.writelines(["Это первая строка текста.\n", "Эта втрая строка.\n"])
# file.close()

# with open('имя_файла', 'режим') as file:
#     text = file.read()
#     print(text)

# with open('example.txt', 'r') as file:
#     text = file.read()

# print(text)


# Задача 1: Чтение содержимого файла
# У вас есть файл example.txt (содержимое файла приведено выше). 
# Напишите программу, которая читает содержимое файла и выводит его на экран.
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

# Задача 2: Подсчет строк в файле
# Напишите программу, которая считает количество строк в файле example.txt.
with open('example.txt', 'r') as file:
    lines = file.readlines()
    print(f"Количество строк в файле: {len(lines)}")

# Задача 3: Поиск слова в файле
# Напишите программу, которая ищет слово "Python" в файле example.txt 
# и выводит все строки, где оно встречается.
with open('example.txt', 'r') as file:
    for line in file.readlines():
        if 'Python' in line:
            print(line)

# Задача 4: Запись новых данных в файл
# Добавьте в конец файла example.txt строку:
# "Python делает программирование проще и интереснее."
with open('example.txt', 'a') as file:
    file.write("\nPython делает программирование проще и интереснее.")
print("Строка добавлена в файл.")

# Задача 5: Создание нового файла
# Создайте новый файл new_example.txt и запишите в него строки:
with open('new_example.txt', 'w') as file:
    file.writelines([
        "Это новый файл.\n",
        "Он создан для демонстрации работы с файлами.\n",
        "Python облегчает создание и управление файлами.\n"
    ])

# Задача 6: Подсчет слов в файле
# Напишите программу, которая подсчитывает количество слов в файле example.txt.
print(len(open('example.txt', 'r').read().split()))

with open('example.txt', 'r') as file:
    content = file.read()
    words = content.split()
    print(f"Количество слов в файле: {len(words)}")


# Задача 7: Извлечение только цитат
# Из файла example.txt извлеките только строки с цитатами (секция 3).
with open('example.txt', 'r') as file:
    for line in file:
        if line.startswith('Секция') or line.startswith("-"):
            print(line.strip())

# with open('example.txt', 'r') as file:
#     for line in file:
#         if line.startswith('- "'):
#             print(line.strip())


# Задача 8: Обратный порядок строк
# Создайте новый файл reversed_example.txt, где строки из example.txt 
# будут записаны в обратном порядке.

# Задача 9: Удаление пустых строк
# Создайте новый файл cleaned_example.txt, в
# котором из файла example.txt удалены все пустые строки.

# Задача 10: Чтение файла поблочно
# Напишите программу, которая считывает содержимое файла example.txt
# по 100 символов за раз и выводит их на экран.