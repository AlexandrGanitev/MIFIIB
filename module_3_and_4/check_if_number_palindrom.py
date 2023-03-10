# Задание 4.4.9
# Дано натуральное восьмизначное число. Выясните, палиндром ли оно (читается одинаково слева направо и справа налево).
#
# (Подсказка: использовать целочисленное деление и деление с остатком не нужно. Попробуйте преобразовать число к строке,
# а потом перевернуть эту строку. См. материал прошлого модуля).

num = input("Введите восьмизначное число --> ")

list_of_strings = num.split() # список строковых представлений чисел
# print(list_of_strings)
list_of_numbers = list(map(int, list_of_strings)) # список чисел
print(list_of_numbers)

if len(list_of_numbers) < 8 or len(list_of_numbers)> 8:
    print("Вы ввели не 8-значное число")
if num == num[::-1]:
    print(f"Это число {num} - палиндром")
else:
    print(f"Число {num} не палиндром")

print('*' * 25, "Вариант 2")
num2 = list_of_numbers
print((num2) == (num2)[::-1])
