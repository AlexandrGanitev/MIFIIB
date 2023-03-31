import timeit

# map + filter
some_list = [i - 10 for i in range(20)]


def pow2(x) : return x ** 2


def positive(x) : return x > 0


print(some_list)
print(list(map(pow2, filter(positive, some_list))))

print('*' * 25, "Короткий вариант с List comprehension/Генератором списка: ")

print([i**2 for i in some_list if i > 0])
print('*' * 25)
squares = [x*x for x in range(10)]
print(squares) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print('*' * 25, "С использованием lambda: ")
squares = list(map(lambda x: x*x, range(10)))
print(squares)
print('*' * 25)
symbols = ['a', 'b', 'c']
values = [1, 2, 3]
for x in symbols:
  print(x)
  squared = [x*x for x in values] # Все плохо. "x" из верхнего "for" затёрт
  print(x)
symbols = ['a', 'b', 'c']
values = [1, 2, 3]
for x in symbols:
  print(x)
  squared = map(lambda x: x*x, values) # Все норм, это локальная область видимости
  print(x)
