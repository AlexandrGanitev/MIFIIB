# Эта функция выводит текст из песни В.Цоя.
# Метод read() — сохраняет всё содержимое файла как строку.
# Он выдает текст так, как он выглядит в файле, т.е. без лишних пробелов.
def read():
    my_file = open('Legend.txt')
    print(my_file.read(184)) #  печать заданного количесва символов, если передать () - выводиться весь текст
    # print(my_file.read())
    print('*' * 25)


# Метод readline() читает файл построчно. В него можно передавать число,
# и из строки будет прочитано указанное число символов.
def readline():
    my_file = open('Legend.txt')
    for i in range(6):
        print(my_file.readline())
    print('*' * 25)


# Метод readlines() вернёт список, в котором элементами будут строки из файла.
def readlines():
    my_file = open('Legend.txt')
    print(my_file.readlines())
    print('*' * 25)


# Самый часто используемый в реальности способ — чтение файла построчно в цикле for.
def cycle_for():
    my_file = open('Legend.txt')
    for line in my_file:
        print(line)
    print('*' * 25)


read()
readline()
readlines()
cycle_for()

# my_file = open('Legend.txt')
# print(my_file.read())