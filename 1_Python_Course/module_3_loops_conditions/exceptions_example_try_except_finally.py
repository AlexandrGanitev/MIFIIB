try:
    print("Перед исключением")
    a = int(input("a: "))
    b = int(input("b: "))
    c = a / b
    print(c)  # печатаем c = a / b, если всё хорошо
except ZeroDivisionError as e:
    print("После исключения")
else:  # код в блоке else выполняется только в том случае, если код в блоке try выполнился успешно (т.е. не вылетело
    # никакого исключения).
    print("Всё ништяк")
finally:  # код в блоке finally выполнится в любом случае при выходе из try-except
    print("Finally на месте")

print("После После исключения")