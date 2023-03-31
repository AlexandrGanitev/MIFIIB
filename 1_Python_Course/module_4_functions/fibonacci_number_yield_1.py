def fib() :
    a, b = 0, 1
    yield a
    yield b

    while True:
        a, b = b, a + b
        yield b


# for i in fib():
#     print(i)

# for num in fib():
#     print(num)
#     if num > 10000: #  здесь мы останавливаем генератор на определенном значении переменной
#         break

# с помощью метода close() можно закрыть генератор
fib_gen = fib()
fib_gen.close() # закрыли генератор

for i in fib_gen: # цикл не выполниться ни одного раза
    print(i)
