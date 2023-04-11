"""
Задание 4.3.1
Задание на самопроверку.

Создайте функцию-генератор, возвращающую бесконечную последовательность натуральных чисел.
По умолчанию, она начинается с единицы и шагом 1, но пользователь может указать любой шаг и
любое число в качестве аргумента функции, с которого будет начинаться последовательность.
"""
def count(start, step):
    counter = start
    while True:
        yield counter
        counter += step

number = int(input("Введите ваше число: "))
step_user = int(input("Введите шаг: "))
print("Вводим переменную для вызова 'ограниченной' функции генератора")
my_gen_func = count(number, step_user)
# Ограничиваем "бесконечность" нашей функции генератора
for i in range(10):
    print(next(my_gen_func)) # с функцией генератором также работает next

# Функция генератор уже является итератором
id(my_gen_func) == id(iter(my_gen_func))
