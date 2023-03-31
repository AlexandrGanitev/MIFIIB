"""
Задание 4.3.2
Задание на самопроверку.

Создайте генератор цикла, то есть в функцию на входе будет передаваться массив, например,
[1, 2, 3], генератор будет вечно работать возвращая 1 2 3 1 2 3… и так далее.
"""


# def generator_loop(list_entered = []):
#     elem = list_entered
#     while True:
#         yield elem
#
# list_ = list(input("Введите массив-список чисел, через пробел: "))
# for element in generator_loop(list_):
#     print(list_)

def repeat_list(list_) :
    list_values = list_.copy()
    while True :
        value = list_values.pop(0)
        list_values.append(value)
        yield value


for i in repeat_list([1, 2, 3]):
    print(i, end='')
# To print on the same line in Python, add a second argument, end=' ', to the print() function call.
# print(i, end=' ')
