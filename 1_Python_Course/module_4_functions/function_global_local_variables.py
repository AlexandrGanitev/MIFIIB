x = 3


def function() :
    print(x)
    return x


print(function())
print('*' * 25)
# x = 3
#
#
# def func():
#     print(x)
#     x = 5
#     x += 5
#     return x
#
#
# print(func())
# UnboundLocalError: local variable 'x' referenced before assignment
print('*' * 25, "Вариант с глобалной переменной")
x = 3


def func():
    global x  # объявляем, что переменная является глобальной
    print(x)
    x = 5
    x += 5
    return x


func()
print(x)
