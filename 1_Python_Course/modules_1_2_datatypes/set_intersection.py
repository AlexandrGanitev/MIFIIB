a = input("Введите первую строку: ")
b = input("Введите вторую строку: ")

a_set, b_set = set(a), set(b) # используем множественное присваивание
print("Выводим объединение множеств:")
a_and_b = a_set.union(b_set)
print("Выводим пересечение множеств:")
a_and_b = a_set.intersection(b_set)
print(a_and_b)