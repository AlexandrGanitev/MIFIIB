# Пусть на вход программы поступает массив из произвольного количества целых чисел и ещё одно целое число,
# которое будем проверять на вхождение в этот массив. Задача состоит в том, чтобы вернуть индекс первого
# вхождения элемента, если он входит в него, и False если не входит.

def find(array, element) :
    for i, a in enumerate(array) :
        if a == element :
            return i
    return False


print("Mассив - это динамический список, повторение - мать учения!")
array = list(map(int, input("Введите элементы массива через пробел: ").split()))
element = int(input("Введите элементы, вхождение в массив которого мы проверяем: "))

print(find(array, element))

print("Ещё раз напоминаю про функцию map(): ")
print("string = input('Введите числа через пробел:')")
print("list_of_strings = string.split() # список строковых представлений чисел")
print("list_of_numbers = list(map(int, list_of_strings)) # список чисел")