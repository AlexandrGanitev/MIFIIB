"""
Задание 4.1.5
Задание на самопроверку.

Напишите функцию, которая будет возвращать количество делителей числа а.

Пример ввода: 5

Пример вывода программы: 2
"""
def dividers_counter(a):
    counter_dividers = 0
    for num in range(1, a + 1):
        if a % num == 0:
            print("Печатаю делитель числа - ", num)
            counter_dividers += 1
    return counter_dividers

entered_number = int(input("Введите ваше число: "))
print(f"У вашего числа {entered_number} такое количество делителей - ", dividers_counter(entered_number))

