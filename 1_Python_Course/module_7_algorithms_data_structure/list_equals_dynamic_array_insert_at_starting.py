"""
Несколько иная ситуация стоит при вставке элемента в начало массива.
Задание 1. Модифицируйте проведенный эксперимент таким образом, чтобы он
проводил измерения времени на тех же самых размерах массива. Анализу подлежит
операция вставки элемента в начало массива.

"""
import timeit


def elapsed_time(func, size):
    return timeit.timeit(func % size, number=100)/100


code_insert = """
elements = range(%d)
array = []
for e in elements:
    array.insert(0,e)
"""

for s in range(10,15):
    measure_1 = elapsed_time(code_insert, 2**s)
    measure_2 = elapsed_time(code_insert, 2**(s+1))
    ratio = measure_2 / measure_1
    print("[%d]/[%d] -> %5.2f" % (2**(s+1), 2**s, ratio))

