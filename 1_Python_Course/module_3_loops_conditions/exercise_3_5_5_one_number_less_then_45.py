# Задание 3.5.5
# Запишите условие, которое является истинным, когда только одно из чисел А, В и С меньше 45.
# Иногда проще записать все условия и не пытаться упростить их.
A = int(input("Введите число A:\t"))
B = int(input("Введите число B:\t"))
C = int(input("Введите число C:\t"))

if ((A < 45) and (B >= 45) and (C >=45)) or \
    ((A >= 45) and (B < 45) and (C >=45)) or \
    ((A >= 45) and (B >= 45) and (C < 45)):
    print('Есть число меньше 45 и только одно')
else:
    print('Числа меньше 45 нет или их несколько')
