numbers_divisible_by_three = [3, 6, 9, 12, 15]

for num in numbers_divisible_by_three:
    quotient = num / 3
    print(f"{num} делиться на 3, результат {int(quotient)}.")
print('*' * 25)
"""
Введение в range()
Итак, как работает функция Python под названием range? Простыми словами, range() позволяет вам генерировать ряд чисел
 в рамках заданного диапазона. В зависимости от того, как много аргументов вы передаете функции, вы можете решить, 
 где этот ряд чисел начнется и закончится, а также насколько велика разница будет между двумя числами.
"""
for i in range(3, 16, 3):
    quotient = i / 3
    print(f"{i} делиться на 3, результат {int(quotient)}.")

print('*' * 25, "Reversed")
for i in reversed(range(5)):
    print(i)