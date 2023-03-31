is_rainy = True  # дождь будет
heavy_rain = False  # не сильный дождь

if is_rainy:
    # в данный блок дописали ещё один условный оператор
    if heavy_rain:
        print("Брать зонт")
    else:
        print("Надеть дождевик")
else:
    print("Не брать зонт")

print('*' * 25)
print("Проверка на равенство числа 0, пустую строку, пустой список:")
print(bool(0))  # False
print(bool(1))  # True

print(bool("")) # False
print(bool("1"))  # True

print(bool([])) # False
print(bool([1]))  # True
print('*' * 25)
zero = 0
# Плохо
if zero != 0:
   print(10 / zero)
else:
   print("Делить на ноль нельзя")

# Хорошо
if zero:
   print(10 / zero)
else:
   print("Делить на ноль нельзя")
print('*' * 25)
# Плохо
password = input("Введите ваш пароль:")
if password == "":
   print("Вы забыли ввести пароль")
else:
   print("Молодец, ввел пароль")

# Очень плохо
if len(password) == 0:
   print("Вы забыли ввести пароль")
else:
   print("Молодец, ввел пароль")

# Хорошо
if not password:
   print("Вы забыли ввести пароль")
else:
   print("Молодец, ввел пароль")