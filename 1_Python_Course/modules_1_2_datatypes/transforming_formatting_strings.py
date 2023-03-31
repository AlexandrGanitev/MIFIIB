int_num = int(input("Введите целое число: ")) # вводим, например, 256
print(int_num)
# 256
print(type(int_num)) # убеждаемся, что тип данных в переменной - int
# <class 'int'>

age = 46
my_age = "I'm " + str(age)
print(my_age)
# I'm 25

wow = 'wow'
print(wow*5) # никакой ошибки не возникает
# wowwowwowwowwow

# шаблон_строки % (переменные)
my_age = "I'm %d years old" % (age) # в шаблоне присутствует специальный символ %d

print(my_age)
# I'm 25 years old
print('*' * 20)
day = 14
month = 2
year = 2012

print("%d.%02d.%d" % (day, month, year))
# 14.02.2012
print("%d-%02d-%d" % (year, month, day))
# 2012-02-14
print("%d/%d/%d" % (year, day, month))
# 2012/14/2

"""Как должен выглядеть шаблон строки для вывода времени в записанном ниже формате?
HH:MM:SS
Вставьте нужный шаблон вместо знаков "???"
print("???"% (hours, minutes, seconds))"""
hours = 12
minutes = 45
seconds = 38
print("%d:%d:%d" % (hours, minutes, seconds))