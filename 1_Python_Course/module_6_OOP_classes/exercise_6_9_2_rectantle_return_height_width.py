# Задание 6.9.2
# Напишите код для описания геометрической фигуры.
# Создайте класс «прямоугольник» с помощью метода  __init__(). На выходе в консоли вам необходимо
# получить длину и ширину с итоговыми значениями.

class Rectangle :
    def __init__(self, l, w) :
        self.leng = l
        self.width = w

    def output_to_console(self) :
        print(f"Длина прямоугольника {self.leng} и ширина {self.width} ")

    def area_rect(self) :
        return int(self.leng * self.width)


l = int(input("Введите длину вашего прямоугольника: "))
w = int(input("Введите ширину вашего прямоугольника: "))
rect = Rectangle(l, w)
rect.output_to_console()

print("Площадь данного прямоугольника равна: ", rect.area_rect(), "см2")
print("С использованием под/надстрочного индекса: ")
print("The area of your rectangle is {} cm\u00b2".format(rect.area_rect()))
