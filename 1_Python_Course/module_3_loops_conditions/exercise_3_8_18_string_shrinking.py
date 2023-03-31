"""
Задание 3.8.18
Задание на самопроверку.

Реализуйте программу, которая сжимает последовательность символов. На вход подается последовательность вида:

aaabbccccdaa
Необходимо вывести строку, состоящую из символов и количества повторений этого символа. Вывод должен выглядеть как:

a3b2c4d1a2
"""
string_letters = input("Введите строку символов: ")
count_letters = 0
first_element = string_letters[0]
new_string = ''
# Вариант 1, не идет из-за "list indices must be integers or slices, not str"
# for i in string_letters:
#     if i == string_letters[i]: тут не нужно индексирования, мы работаем со строкой
#         count_letters += 1
#         new_list.append(int(i) + count_letters)
# new_list = list(new_list)
print("Ваша введенная буквенная строка: ", string_letters)
# Вариант 2, сотворим 2 списка из уникальных элементов и счетчика и соединим их
for c in string_letters:  # равносильно выражению for i in [0, 1, 2, 3, 4, 5, 6]:
    # print("Индекс элемента: ", i)
    # print("Значение элемента: ", string_letters[i])  # с помощью индекса получаем значение элемента
    # print("---")
    if c == first_element:
        count_letters += 1
    else:
        new_string += first_element + str(count_letters)
        first_element = c
        count_letters = 1
new_string += first_element + str(count_letters)
print(new_string)
print('*' * 25, "Вариант 3")
text = input("Введите строку: ")  # получаем строку

first = text[0]  # сохраняем первый символ
count = 0  # заводим счетчик
result = ''  # и результирующую строку

for c in text :
    if c == first :  # если символ совпадает с сохраненным,
        count += 1  # то увеличиваем счетчик
    else :
        result += first + str(count)  # иначе - записываем в результат
        first = c  # и обновляем сохраненный символ с его счетчиком
        count = 1

result += first + str(count)  # и добавляем в результат последний символ
print(result)

