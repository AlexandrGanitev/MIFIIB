"""
Задание 4.4.7
Дано двузначное число. Определить, входит ли в него цифра 5. Попробуйте решить задание с использованием
целочисленного деления и деления с остатком."""
num = int(input("Введите двузначное число -->"))
# check if the number is 2-digit:
# if len(list(num)) > 2:
#     print("Вы ввели не двузначное число. Запустите программу ещё раз.")

digit1 = num // 10
digit2 = num % 10
print("Первая и вторая цифры: ", str(digit1) + " и " +str(digit2))
if ((digit1 == 5) or (digit2 == 5)):
    print("Данное число содержит цифру 5!")