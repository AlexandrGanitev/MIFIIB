"""
Задание 4.2.4
С помощью рекурсивной функции разверните строку.
"""


def recursion_string(str_):
    if len(str_) == 0:
        return ''
    else:
        return str_[-1] + recursion_string(str_[:-1])


my_string = input("Введите строку...\n")
print(my_string[:-1])
print(recursion_string(my_string))
