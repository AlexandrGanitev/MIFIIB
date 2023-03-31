import random

"""
Задание 4.5.9
Задание на самопроверку.

Напишите рекурсивную функцию, находящую минимальный элемент списка без использование циклов и 
встроенной функции min().
"""


def generate_list(length: int) -> list:
    gen_lst = ''.join(str(random.randint(0, 9)) for _ in range(length))
    # print(type(gen_lst))
    gen_lst = [int(x) for x in gen_lst]  # надо было привести сгенерированный список str к списку чисел int
    return list(gen_lst)  # возвращаем список int


def minimal_element(a_list: list) -> list[str] :
    if len(a_list) == 1 :
        return a_list[0]
    return a_list[0] if a_list[0] < minimal_element(a_list[1 :]) else minimal_element(a_list[1 :])


if __name__ == '__main__' :
    my_list = generate_list(15)
    print("Наш сгенерированный список: ", my_list)
    print("Минимальным элемент этого списка: ", minimal_element(my_list))

print('*' * 25, "Вариант 2, короткий")


def min_list(L) :
    if len(L) == 1 :
        return L[0]
    return L[0] if L[0] < min_list(L[1 :]) else min_list(L[1 :])


list_ = [7, 2, 4, 0, 1, 3, -4]
print("Наш список: ", list_)
print("Минимальным элемент этого списка: ", min_list(list_))
