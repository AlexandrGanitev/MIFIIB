"""
Задание 4.5.11
Задание на самопроверку.
Поработаем над более сложной рекурсивной функцией. Сейчас попробуем реализовать функцию equal(N, S),
проверяющую, совпадает ли сумма цифр числа N с числом S. При написании программы следует обратить
внимание на то, что, если S стала отрицательной, то необходимо сразу вернуть False.
Реализуйте описанную выше функцию.
"""


def equal(N, S) :
    if S < 0 :
        return False
    if N < 10 :
        return N == S
    else :
        return equal(N // 10, S - N % 10)


def sum_digit(n) :  # здесь функция не суммирует до конца, например 11 будет = 2, см. второй вариант...
    if n < 10 :
        return n
    else :
        return sum_digit(n % 10 + sum_digit(n // 10))


my_number = int(input("Введите натуральное число состоящее из n цифр: \n"))
number_s = int(input("Введите некое число S: \n"))
N = sum_digit(my_number)
print("Сумма чисел вашего натурального числа = ", N)
print("Равны ли N и S? ", equal(N, number_s))