# Задание 4.6.2
# Задание на самопроверку.
#
# Гипотеза Сиракуз гласит, что любое натуральное число сводимо к единице при следующих действиях над ним:
#
# 1) если число чётное — разделить его пополам;
# 2) если нечётное — умножить на 3, прибавить 1 и результат разделить на 2.
# Над вновь полученным числом повторить действия п. 1 или п. 2 в зависимости от его чётности. Рано или поздно
# число станет равным 1. Проверить эту гипотезу.

n = int(input("Введите число: \n"))

while True :
    if n % 2 == 0:
        n = n // 2
    else:
        n = (n * 3 + 1) // 2
    print(n)

    if n == 1:
        print("Число сведено к 1!")
        break
