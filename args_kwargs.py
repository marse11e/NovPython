from os import system
system("clear")


# a = (1, 2, 3, "aslkdnm")
# b = (4, *a, 5, 6, *a)
# print(b)

# def test(a, b=10, *args):
#     print(a)
#     print(b)
#     print(args)
#     return a, b, args

# test(1, 2, True, 9, 10)

# def num_sum(*numbers):
#     print(numbers)
#     return sum(numbers)

# print(num_sum(1, 2, 3, 4, 5))


# def test(a, b=10, *args, **kwargs):
#     print(a)
#     print(b)
#     print(args)
#     print(kwargs)
#     return a, b, args, kwargs

# test(1, 2, True, 9, 10, {'name': 123}, name="John", age=30)




# def info(name, age):
#     return f"Name: {name}, Age: {age}"

# i = {"name": "John", "age": 30}

# print(info(**i))



# def add_n(x, y):
#     return x + y

# print(add_n(1, 2))
add_n = lambda x, y: x + y

even_n = lambda x: x if x % 2 == 0 else "odd"

# print(even_n(5))
# print(add_n(1, 2))
nums = [1, 2, 3, 4, 5, 0]
# l_even = list(filter(lambda n: n % 2 == 0, nums))
# s_nums = list(map(bool, nums))
v = sorted(nums, reverse=True)
print(v)




