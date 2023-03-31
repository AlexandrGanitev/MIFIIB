"""Задание 2.5.15
Напишите программу, которая на вход получает две последовательности целых чисел,
а возвращает список элементов, встречающихся только в одной из последовательностей.
Какую операцию над множествами вы использовали? Введи только название метода без скобок
"""
string_nums_a = input("Введите последовательность a чисел через Пробел: ")
string_nums_b = input("Введите последовательность b чисел через Пробел: ")
print("Введенные строковые последовательности a, b:", string_nums_a, " ",string_nums_b)
print("Конвертируем в список строковых представлений чисел")
list_strings_a = string_nums_a.split()
list_strings_b = string_nums_b.split()
print(list_strings_a, list_strings_b)
print("Конвертируем в список чисел")
list_nums_a = list(map(int, list_strings_a))
list_nums_b = list(map(int, list_strings_b))
print(list_nums_a, " ", list_nums_b)
print("Переводим списки в множества")
set_a = set(list_nums_a)
set_b = set(list_nums_b)
print("Множества: ",set_a, set_b)
set_difference_a_b = set_a.difference(set_b)
set_symmetric_difference_a_b = set_a.symmetric_difference(set_b)
print("Разница элементов между двумя строками:",list(set_difference_a_b))
print("А это симметричная разность: ", list(set_symmetric_difference_a_b))

"""Конвертирование введенной строки в строковые представления чисел и потом в список чисел:
string = input("Введите числа через пробел:")

list_of_strings = string.split() # список строковых представлений чисел
# print(list_of_strings)
list_of_numbers = list(map(int, list_of_strings)) # список чисел
print(list_of_numbers)
"""
