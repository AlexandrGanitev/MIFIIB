# Задание 3.5.8
# Проверьте, все ли элементы в списке являются уникальными.

string = input("Введите символы через пробел:")
list_of_strings = string.split() # список строковых представлений символов
print("Список, который мы переводим в множество:", list_of_strings)
b = set(list_of_strings)
print("Наше множество:",b)
print("Обратив список в множество и отсортировав уникальные элементы, обращаем обратно в список:")
b_list = list(b)
print("Отсортированный список уникальных элментов: ", b_list)

print('*' * 25)
list_ = [-5, 2, 4, 8, 12, -7, 5]
print(len(list_) == len(set(list_)))
# Note: я не внимательно читаю задания, второй вариант и есть проверка...