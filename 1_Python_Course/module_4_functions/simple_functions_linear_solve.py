def linear_solve(a, b) :
    return b / a


print(linear_solve(2, 9))
# print(linear_solve(0, 1))
print('*' * 25, "Модификация 2")


def linear_solve(a, b) :
    if a :  # помним, что 0 интерпретируется как False, иначе — True
        return b / a
    else :
        return "Нет корней"


print(linear_solve(2, 9))
print(linear_solve(0, 1))

print('*' * 25, "Модификация 3")


def linear_solve(a, b):
    if a :
        return b / a
    elif not a and not b :  # снова используем числа в логических выражениях
        return "Бесконечное количество корней"
    else :
        return "Нет корней"


print(linear_solve(2, 9))
print(linear_solve(0, 1))
