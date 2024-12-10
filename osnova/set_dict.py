from os import system
system('clear')






# my_list = []
# my_tuple = ()
# my_tuple = 1,



# # SET (множество) - неупорядоченный набор уникальных элементов
# # множества не может внутри себя хранить LIST DICT SET
# # my_list = [1, 3, 2, 5, 4, 6, 7, 8, 9, 10, 1]
# # my_set = {1, 3, 2, 5, 4, 6, 7, 8, 9, 10, 1}
# # my_set2 = set()

# # print(my_list)
# # print(my_set)
# # print(my_set2)




# # my_list = [1, 3, 2, 5, 4, 6, 7, 8, 9, 10, 1]

# # a = set(my_list)
# # print(my_list)
# # print(a)
# # print(list(a))



# n = {1, 1, 1, 2, 3, 3, 5, 5, 4, 4, 'htl', '1'}

# n.add(6)
# n.add('hello')
# # add() - добавляет элемент в множество

# n.remove('hello')
# n.remove('htl')
# # remove() - удаляет элемент из множества

# a = n.pop()
# print(a)
# # pop() - Удаляет начальный или конечный элемент

# n.discard(999)
# # discard() - Удаляет элемент из множества, если он находится в нем

# print(n)




# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}

# # не пересекается ли? не пересекается True. пересекается False
# print(a.isdisjoint(b))
# # isdisjoint() - проверяет есть ли пересечение множеств

# # объединение (НЕ СОРТИРУЕТ) можно сократить знаком |
# print(a.union(b))
# print(a | b) # union

# # Возвращение пересечение. 
# # Вытаскивает только то, что пересекается и СОКРАЩАЕТ 
# print(a.intersection(b))
# print(a & b) # intersection

# # разность (НЕ СОРТИРУЕТ)
# print(a.difference(b))
# print(b.difference(a))
# print(a - b) # difference
# print(b - a) # difference

# # возвращает разность обеих сторон
# print(a.symmetric_difference(b))

# # добавить
# a.add("Hello")

# # удаляет по названию
# a.remove("Hello") 

# # удаляет по индексу
# a.pop() # Не используется для set. Используется для list.

# # очистить
# a.clear()

# print(a)


# DICT (словарь) - неупорядоченный набор пар ключ-значение
# ключи должны быть уникальными

# my_dict = {
#     'name': 'Marselle', 
#     'surname': 'Naz',
# }
# print(my_dict['name'])
# print(my_dict['surname'])



# info = {
#     'name': 'Marselle',
#     'surname': 'Naz',
#     'email': 'marselle.naz@yandex.kz',
#     'phone': '+7 (747) 056 06 79',
#     'uni': 'PIEC - ОшМу',
#     'job': 'Python BackEnd Developer',
#     'birth': '01.05.2003',
#     'messager': {
#         'telegram': 'MarselleNaz',
#         'instagram': 'marselle.naz',
#         'linkedin': 'marselle.naz',
#     },
#     'banks': ['kaspi', 'mbank', 'jusan', 'tinkov'],
#     'passwords': ('321456', '%^&*Mars', 'di_naz'),
#     'address': {
#         'country': 'Kz',
#         'region': 'Almaty obl',
#         'city': 'Almaty',
#         'street': 'Kanysha Satpaeva',
#         'house': {
#             'number': '90/52',
#             'entrance': 1,
#             'floor': 15,
#             'flat': 156
#         },
#     },
# }

# print(info.get('uni'))
# print(info.get('banks')[0])
# print(info.get('bank', 'Нет такого ключа'))
# print(info.get('address').get('house').get('flat'))
# print(info['address']['house']['number'])
# print(info['messager']['instagram'])


# info['messager']['instagram'] = 'MarselleNaz'

# print(info['messager']['instagram'])


# info['address']['house']['flat'] = 100

# print(info.get('address').get('house').get('flat'))
# print(info.get('address')['house']['flat'])
# print(info['address']['house']['flat'])


# info['address'] = {
#         'country': 'Kz',
#         'region': 'Almaty obl',
#         'city': 'Almaty',
#         'street': 'Kazybek Bi',
#         'house': {
#             'number': '185',
#             'entrance': 5,
#             'floor': 3,
#             'flat': 55
#         },
#     }

# print(info['address'])



a = {
    'name': 'Eduard',
    'age': 12
}
# Показывает только ключи
print(a.keys())

# Показывает только значения
print(a.values())

# Показывает ключи и значения одновременно. 
# Ключи и значения разделены запятой.
print(a.items())

# print(a['age'])

# a['age'] = 22
# print(a['age'])

# # Добавляет значения из другого словаря в текущий если ключа нет.
# a['age1'] = 66
# print(a)

# # Добавляет значения из другого словаря в текущий.
# a.update({'surname': 'Naz'})
# print(a)

# # Удаляет по ключу словаря dict
# age = a.pop('age')
# print(age)
# print(a)


a = {1, 23, 345, 56, 7}
a.discard(7)
print(a)

b = {23, 1, 32, 33}
c = {1, 2, 3, 4, 5, 6}

print(a.intersection(b))
print(a & c)


print(c - b)


set4 = {1, 2, 3, 4, 5}
el = set4.pop()
print(el, set4)

