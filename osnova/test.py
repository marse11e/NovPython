# "The greatest victory is that which requires no battle"
# "battle no requires which that is victory greatest The"





# text = "The greatest victory is that which requires no battle".split()
# text.reverse()
# print(" ".join(text))


# Для строки "a **& cZ":

# Присутствуют буквы a, c и z.
# Результат: "10100000000000000000000001".
# Для строки "aaaaaaa79345675":

# Присутствует только a.
# Результат: "10000000000000000000000000".
# Для строки "&%#*":

# Букв нет.
# Результат: "00000000000000000000000000".








# def is_pronic(n):
#     for i in range(n+1):
#         if i*(i+1) == n:
#             return True
#     return False

# print(is_pronic(1))
# print(is_pronic(2))
# print(is_pronic(3))
# print(is_pronic(4))
# print(is_pronic(5))
# print(is_pronic(6))
# print(is_pronic(-3))
# print(is_pronic(-27))


# def change(st: str):
#     al = 'abcdefghijklmnopqrstuvwxyz'
#     res = ''

#     for letter in al:
#         if letter in st.lower():
#             res += '1'
#         else:
#             res += '0'
        
#     return res

# def change(st: str):
#     return ''.join(['1' if letter in st.lower() else '0' for letter in 'abcdefghijklmnopqrstuvwxyz'])

# print(change("a **&aaaaad  bZ"))
# change('Abc e  $$  z')
# change("!!a$%&RgTT")
# change("")
# change("abcdefghijklmnopqrstuvwxyz")
# change("aaaaaaaaaaa")
# change("&%&%/$%$%$%$%GYtf67fg34678hgfdyd")



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

login = 'admin' 

print(login in users.keys() and 'admin@123' == users['admin']['config']['password'])