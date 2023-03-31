#  Задание 7.7.1
# Задание на самопроверку.
#
# Напишите функцию count, которая возвращает количество вхождений элемента в массив

def count(array, element) :
    count = 0
    for elem in array :
        if elem == element:
            count += 1
    return count


print("Mассив - это динамический список, повторение - мать учения!")
array = list(map(int, input("Введите элементы массива через пробел: ").split()))
element = int(input("Введите элементы, вхождение в массив которого мы проверяем: "))

print(count(array, element))
