d = {2 : "c", 1 : "d", 4 : "a", 3 : "b"}

# Чтобы отсортировать его по ключам, нужно сделать так:
print(dict(sorted(d.items())))  # {1: 'd', 2: 'c', 3: 'b', 4: 'a'}
print('Другой вариант с lambda: ')
sorted_with_lambda = dict(sorted(d.items(), key=lambda x : x[1])) # сортировка по значению: 'а', 'b'...
# если убрать dict(), то результат будет кортежем - [(4, 'a'), (3, 'b'), (2, 'c'), (1, 'd')]
print(sorted_with_lambda)  # [(4, 'a'), (3, 'b'), (2, 'c'), (1, 'd')]
