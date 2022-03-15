MAX_CHAR_LENGTH = 128


def reverse(name: str) -> str:
    x = 100
    print(name, x)
    return name[::-1].title()


print(reverse("henry"))

#
# def print_reverse(name: str) -> None:
#     print(reverse(name))
#
#
# names = ["Henry", "Marina", "Emma", "Jo", "Katie"]
#
# for name in names:
#     print(print_reverse(name))

# def my_function(arg1, arg2):
#     return arg1 + " " + arg2 + "!"
#
# print(my_function("Hello", "World"))

# import random
#
# random.seed()
#
# def print_random():
#     print(random.random())
#
# def print_range(say_hello=False, max=10):
#     for i in range(max):
#         if say_hello:
#             print("Hello")
#         print("*" * i)
#
#
#
#
# print_range(max=5, say_hello=True)


