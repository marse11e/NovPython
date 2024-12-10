from os import system
system('clear')


# try:
#     # Код, который может вызвать ошибку

# except ТипОшибки:
#     # Код, который выполняется, если ошибка произошла

# else:
#     # Код, который вызван без ошибок

# finally:
#     # Срабатывает всегда
# num = int(input('Введите число: '))
# print(num)



# try:
#     num = int(input('Введите число: '))
#     print(num)

# except Exception as ex:
#     print("Вводить можно только числа", ex)
# try:
#     n = int(input('Введите число: '))
#     n2 = int(input('Введите число 2: '))

# except ValueError:
#     print("Вводить можно только числа")

# except ZeroDivisionError:
#     print("Нельзя делить на ноль")

# except KeyboardInterrupt:
#     print("\nВыход из программы")

# else:
#     print(n / n2)

# finally:
#     print("Конец программы")


users = {
    "admin": {
        "config": {
            "email": "admin@azure.kz",
            "password": "admin@123",
        },
        "data": {
            "name": "Admin",
            "surname": "Admin",
            "phone": "+77475556677",
            "address": "Almaty",
            "balance": 99999999999999999
        },
    }
}

auth_user = None

while True:
    print("""
1. Авторизоваться
2. Зарегистрироваться
3. Баланс
4. Перевести деньги
5. Все пользователи
6. Выход
    """)
    choise = input("Выберите пункт: ")

    if choise == '1':
        login = input("Введите логин: ")
        password = input("Введите пароль: ")

        if login in users.keys() and password == users[login]['config']['password']:
            print("Вы успешно авторизовались")
            auth_user = login
        else:
            print("Неверный логин или пароль")
    elif choise == '2':
        if auth_user is not None:
            print("Вы уже авторизованы")
            continue

        login = input("Придумайте логин: ")

        while login in users.keys():
            print("Такой логин уже существует")
            login = input("Придумайте логин заново: ")

        password = input("Придумайте пароль: ") 
        password2 = input("Повторите пароль: ")

        while password != password2:
            print("Пароли не совпадают")
            password = input("Придумайте пароль заново: ")
            password2 = input("Повторите пароль заново: ")
        else:
            email = input("Введите email: ")
            name = input("Введите имя: ")
            surname = input("Введите фамилию: ")
            phone = input("Введите номер телефона: ")
            address = input("Введите адрес: ")
            balance = 100
        
        users[login] = {
            "config": {
                "email": email,
                "password": password
            },
            "data": {
                "name": name,
                "surname": surname,
                "phone": phone,
                "address": address,
                "balance": balance
            }
        }
            
    elif choise == '3':
        if auth_user is None:
            print("Вы не авторизованы")
            continue

        user_information = f"""
        ФИО: {users[auth_user]['data']['name']} {users[auth_user]['data']['surname']}
        Т. номер: {users[auth_user]['data']['phone']}
        Адрес: {users[auth_user]['data']['address']}
        Баланс: {users[auth_user]['data']['balance']} тенге
        """
        print(user_information)

    elif choise == '4':
        if auth_user is None:
            print("Вы не авторизованы")
            continue
        
        try:
            summu = int(input("Введите сумму: "))
        except ValueError:
            print("Введите сумму правильно.")
            continue

        login_recipient = input("Введите логин получателя: ")
        if login_recipient not in users.keys():
            print("Такого логина не существует")
            continue

        if users[auth_user]['data']['balance'] < summu:
            print("Недостаточно средств")
            continue
        else:
            users[auth_user]['data']['balance'] -= summu
            users[login_recipient]['data']['balance'] += summu
            print("Перевод выполнен успешно")

    elif choise == '5':
        if auth_user is None:
            print("Вы не авторизованы")
            continue
        
        for k, v in users.items():
            print(f"""
        ФИО: {users[k]['data']['name']} {users[k]['data']['surname']}
        Т. номер: {users[k]['data']['phone']}
        Адрес: {users[k]['data']['address']}
        Баланс: {users[k]['data']['balance']} тенге
            """)
    
    elif choise == '6':
        if auth_user is None:
            print("Вы не авторизованы")
            continue
        else:
            auth_user = None
            print("Вы вышли из аккаунта")
    
    else:
        print("Неверный пункт")
