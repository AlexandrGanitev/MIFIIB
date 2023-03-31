"""
Задание 4.2.3
Задания на самопроверку.

С помощью рекурсивной функции найдите сумму чисел от 1 до n."""


def recursion_sum(n):
    if n == 1:
        return 1 # терминальный случай
    return n + recursion_sum(n-1) # вызов рекурсии

number = int(input("Введите ваше число: "))
print(recursion_sum(number))