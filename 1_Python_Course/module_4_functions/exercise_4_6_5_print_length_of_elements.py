"""
Задание 4.6.5

Замените знаки «?» корректным выражением. Выведите длину каждого элемента в списке.
"""

a = ["asd", "bbd", "ddfa", "mcsa"]

print([len(elem) for elem in a])

print(list(map(len, a)))

for i in map(len, a) :
    pass

a = ["это", "маленький", "текст", "обидно"]

print(list(map(str.upper, a)))
