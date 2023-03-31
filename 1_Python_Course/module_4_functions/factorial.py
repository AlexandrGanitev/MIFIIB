def factorial(n):
    if n == 1:
        return 1

    return n * factorial(n - 1)

number = int(input("Введите ваше натуральное число: "))
print(factorial(number))