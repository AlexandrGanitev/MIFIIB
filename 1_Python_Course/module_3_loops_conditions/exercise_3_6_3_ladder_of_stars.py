"""
Задание 3.6.3
Напишите программу, которая будет печатать лесенку следующего типа:

n = 3
*
**
***

n = 4
*
**
***
****
"""
n = 3
for i in range(1, n + 1):
    print('*' * i)

n = 4
for i in range(1, n + 1):
    print('*' * i)
print('*' * 25)
# В виде функции
def print_ladder(n) :
    # Можно использовать и (start, stop, step) аргументы, если надо
    for i in range( n + 1) :
        print('*' * i)


print_ladder(5)
print_ladder(6)

