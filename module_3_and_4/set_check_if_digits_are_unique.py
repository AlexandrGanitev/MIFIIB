# Задание 4.4.8
# Проверить, все ли элементы в списке уникальны.
#
# (Подсказка: используйте возможности set)

#
# string = input("Введите символы через пробел:")
# list_of_strings = string.split() # список строковых представлений символов
# print("Список, который мы переводим в множество:", list_of_strings)
# b = set(list_of_strings)
# print("Наше множество:",b)
# print("Обратив список в множество и отсортировав уникальные элементы, обращаем обратно в список:")
# b_list = list(b)
# print("Отсортированный список уникальных элментов: ", b_list)

print('*' * 25)
list_ = [-9, 3, 4, 8, 52, -4, 15, 2]
if (len(list_) == len(set(list_))):
    print("Все элементы списка уникальны")