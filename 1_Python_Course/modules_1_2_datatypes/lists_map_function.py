L = [3.3, 4.4, 5.5, 6.6]
print(L)
print("Возможности языка позволяют выполнить определённые действия для каждого элемента списка. "
      "Такую операцию можно проделать с помощью функцию map(),  map(function, list): ")

# печатаем сам объект map
print("к каждому элементу применяем функцию округления:")
print("Печать объекта map: ",map(round, L))
# <map object at 0x7fd7e86eb6a0>
print("и результат его преобразования в список: ")
print(list(map(round, L)))
# [3, 4, 6, 7]
print(list(map(float, L)))
print('*' * 25)

string = input("Введите числа через пробел:")

list_of_strings = string.split() # список строковых представлений чисел
# print(list_of_strings)
list_of_numbers = list(map(int, list_of_strings)) # список чисел
print(list_of_numbers)
# print(list_of_numbers)
# print("Здесь начиная с элемента 0 идем с шагом 3")
# print(list_of_numbers[::3])
# sum() вычисляет сумму элементов списка_numbers[::3])) # sum() вычисляет сумму элементов списка
print(sum(list_of_numbers[::3]))