from os import system
system('clear')


# HyperText Transfer Protocol
# Host: www.google.com
# GET /index.html HTTP/1.1
# User-Agent: Mozilla/5.0
# Accept: json/html
# Url: https://www.google.com/

# json = list | dict
# text = str
# content = bytes | I.O

# Основные HTTP-методы:
# GET: запрос на получение данных с сервера.
# POST: отправка данных на сервер.
# PUT: обновление данных на сервере.
# DELETE: удаление ресурса.

# HEAD: запрос заголовков ресурса.
# OPTIONS: запрос доступных методов для ресурса.


# Статус-коды HTTP:
# 1xx: информационные (например, 101 — Switching Protocols).
# 2xx: успешные запросы (например, 200 — OK).
# 3xx: перенаправления (например, 301 — Moved Permanently).
# 4xx: ошибки клиента (например, 404 — Not Found).
# 5xx: ошибки сервера (например, 500 — Internal Server Error).

# pip install requests
# pip3 install requests

import requests

url = "https://dl.zamp3.net/uploads/music/2020/11/kajrat-nurtas-seni-sujem-mp3.mp3"

# Отправляем зопрос на url и полученный ответ сохраняем в response
response = requests.get(url)
print('Connect' if response.status_code == 200 else 'Error')

with open('Кайреке - Сени Суйем.mp3', 'wb') as file:
    file.write(response.content)

# print(response.text)

# with open('sxodim.html', 'w') as file:
#     file.write(response.text)

# print(response.cookies)
# print(response.headers)
# print(response.connection)
# print(response.history)