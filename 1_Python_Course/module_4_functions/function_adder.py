"""
Давайте рассмотрим задачку и сделаем функцию сумматор, которая будет складывать любое количество
переданных ей аргументов.
"""


def adder(*nums):
    sum_ = 0
    for n in nums:
        sum_ += n

    return sum_


print(adder())  # 0
print(adder(1))  # 1
print(adder(1, 2))  # 3
print(adder(1, 2, 3))  # 6
