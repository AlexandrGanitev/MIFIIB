"""
Задание 4.1.6
Задание на самопроверку.

Напишите функцию, которая проверяет, является ли данная строка палиндромом или нет, и возвращает результат проверки. Пример:

check_palindrome("test")  # False
check_palindrome("Кит на море не романтик")  # True
"""


def check_palindrom(str_):
    if str_ == (str_[::-1]):
        # return "Введенная строка - палиндром"
        return True
    else :
        # return "Строка не палиндром!"
        return False


entered_string = input("Введите вашу строку - ")
entered_string = entered_string.lower()
entered_string = entered_string.replace(" ", "")
entered_string = entered_string.replace("\n", "")
print(check_palindrom(entered_string))
