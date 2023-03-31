# Из заданного списка вывести только положительные элементы
def positive(x) :
    return x > 0  # функция возвращает только True или False


result = filter(positive, [-2, -1, 0, 1, -3, 2, -3])
print(type(result)) # <class 'filter'>
# Возвращается итератор, т.е. перечисляйте или приводите к списку
print(list(result))  # [1, 2]
