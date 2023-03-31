def first_gen(input_) :
    yield input_
    input_ += 1
    print(input_)


my_first_gen = first_gen(5)
print(next(my_first_gen))
# print(next(my_first_gen))
print(my_first_gen)
print('*' * 25, "Второй вариант генератора: ")


def second_gen(input_) :
    yield input_
    input_ += 1

    yield input_
    input_ += 1

    return input_


my_second_gen = second_gen(10)
print(next(my_second_gen))
print(next(my_second_gen))
# print(next(my_second_gen)) # окончание итерирования
print('*' * 25, "Третий вариант генератора: ")


def last_gen() :
    for i in range(10) :
        yield i
        if i == 5 :
            raise StopIteration


my_last_gen = last_gen()

for _ in range(10) :
    print(next(my_last_gen))

# for перехватывает исключение
my_last_gen = last_gen()
for i in my_last_gen :
    print(i)
