def twice_func(inside_func) :
    """Функция, выполняющая дважды функцию принятую в качестве аргумента"""
    inside_func()
    print('*' * 25)
    inside_func()


def hello() :
    print("Let's calculate!", end=' ')  # добавил end здесь, чтобы избавиться от пробела между строками
    for i in range(5) :
        print(i * '#')
    print("Hello")
    print('------')


twice_func(hello)
# Hello - так было в основном варианте, где была только печать hello
# Hello
