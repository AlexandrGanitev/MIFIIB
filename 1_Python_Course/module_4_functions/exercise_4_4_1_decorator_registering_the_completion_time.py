import time

"""
Возьмите из этого примера декорированные функции, которые возвращают время работы основной 
функции и найдите среднее время выполнения для 100 выполнений каждой функции.
"""
N = 100


def decorator_time(fn) :
    def wrapper() :
        print(f"Запустилась функция {fn}")
        t0 = time.time()
        result = fn()
        print(f"Результат шычисления переданной функции {fn}", result)
        dt = time.time() - t0
        print(f"Функция выполнилась. Время: {dt:.10f}")
        return dt  # задекорированная функция будет возвращать время работы

    return wrapper


def pow_2() :
    return 10000000 ** 2


def in_build_pow() :
    return pow(10000000, 2)


pow_2 = decorator_time(pow_2)
in_build_pow = decorator_time(in_build_pow)

mean_pow_2 = 0 # добавили переменную среднего значения и присвоили ей нулевое значение
mean_in_build_pow = 0
for _ in range(N): # _ перебирает итерируемые элементы, чтобы не использовать индекс
    mean_pow_2 += pow_2()
    mean_in_build_pow += in_build_pow()

print(f"Функция {pow_2} выполнялась {N} раз. Среднее время: {mean_pow_2 / N:.10f}")
print(f"Функция {in_build_pow} выполнялась {N} раз. Среднее время: {mean_in_build_pow / 100:.10f}")

# Using "_" as variable for iteration
# 1. To hold the result of the last executed statement in an interactive interpreter session.
# This precedent was set by the standard CPython interpreter, and other interpreters have followed suit
# 2. For translation lookup in i18n (imported from the corresponding C conventions, I believe),
# as in code like:
# raise forms.ValidationError(_("Please enter a correct username"))
# 3. As a general purpose "throwaway" variable name to indicate that part of a function result is
# being deliberately ignored, as in code like:
#  label, has_label, _ = text.partition(':')