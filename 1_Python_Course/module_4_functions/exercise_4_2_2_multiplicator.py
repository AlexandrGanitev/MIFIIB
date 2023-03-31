"""
Задание 4.2.2
Задание на самопроверку.

Написать функцию, которая будет перемножать любое количество переданных ей аргументов.
"""
def multiplier(*nums):
    result = 1
    for n in nums:
        result *= n

    return result

print(multiplier(1))
print(multiplier(1, 3, 9))
print(multiplier(3, 14, 123))
print(multiplier(0, 2, 5))

