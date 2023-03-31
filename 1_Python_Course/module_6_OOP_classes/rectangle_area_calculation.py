from rectangle import Rectangle, Square, Circle
# далее создаём два прямоугольника

rect_1 = Rectangle(3, 4)
rect_2 = Rectangle(12, 5)

# Вывод площади наших двух прямоугольников
print(rect_1.get_area())
print(rect_2.get_area())


# Подсчитаем площади квадратов
square_1 = Square(5)
square_2 = Square(10)
print(square_1.get_area_square(), square_2.get_area_square())
print('*' * 25, "Продолжаем работать с нашими данными, переносим объекты в коллекцию figures")

figures = [rect_1, rect_2, square_1, square_2]

for figure in figures:
    if isinstance(figure, Square):
        # print(figure) – checking if this object is of the type Square:
        print(figure.get_area_square())
    else:
        print(figure.get_area())

print('*' * 25, "Расчитываем площадь круга")
circle_1 = Circle(10)
circle_2 = Circle(15)
print(circle_1.get_area_circle(), circle_2.get_area_circle())