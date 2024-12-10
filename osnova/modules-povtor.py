# import test
# from test import (
#     a, b, name, surname
# )

# print(a)
# print(b)
# print(name)
# print(surname)

# from datetime import datetime

# print(datetime.now().year)
# print(datetime.today().minute)

# print(datetime.now().date())
# print(datetime.now().time())

from random import (
    choice, choices, 
    random, randint, 
    shuffle, sample,
    randrange
)

# a = [1, 2, 3, 4]
# # print(choice(a))

# # print(choices(a, k=3))
# # print(sample(a, k=3))
# # shuffle(a)
# # print(a)
# # print(randint(1, 10))
# # print(random())
# # print(randrange(1, 10, 2))


# # name = "marselle"

# # my_list = ['name', 'surname']

# # for element in my_list:
# #     print(element)

# #     for i in element:
# #         print(i)






# p = input("Enter a PASSWORD: ")
# p2 = input("Enter a PASSWORD 2: ")

# while p != p2:
#     print("Passwords do not match")
#     p = input("Enter a PASSWORD: ") 
#     p2 = input("Enter a PASSWORD 2: ")
# else:
#     print("Passwords match")




# a = 0
# while a != 10:
#     a += 1
#     print(a)

while True:
    n = int(input("Enter a number: "))
    n2 = int(input("Enter a number 2: "))
    op = input("Enter an operation (+ / * -): ")

    if op == "+":
        print(n + n2)
    elif op == "-":
        print(n - n2)
    elif op == "*":
        print(n * n2)
    elif op == "/":
        if n2 != 0:
            print(n / n2)
        else:
            print("Cannot divide by zero")
    else:
        print("Invalid operation")