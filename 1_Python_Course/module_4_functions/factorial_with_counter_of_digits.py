def factorial(n) :
    if n == 1 :
        return 1

    return n * factorial(n - 1)


number = int(input("Введите ваше натуральное число: "))
factorial_result = factorial(number) # создаём переменную, которая будет хранить значение факториала, в формате int
print(factorial_result)
print(len(str((factorial_result)))) # переводим в строку и определяем длину(количиство элементов)
