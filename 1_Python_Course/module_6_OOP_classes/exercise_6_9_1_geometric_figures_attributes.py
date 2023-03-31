# Создайте класс любых геометрических фигур, где на выход мы получаем характеристики фигуры.
# Каждый экземпляр должен иметь атрибуты, которые зависят от выбранной фигуры. Например,
# для прямоугольника это будут аргументы x, y, width и height.
#
# Кроме того вы должны иметь возможность передавать эти атрибуты при создании объекта класса.
#
# Создайте метод, который возвращает атрибуты вашей фигуры в виде строки.
#
# Для реализации используйте str. К примеру, для объекта «прямоугольник» со значениями атрибутов
# x = 5, y = 10, width = 50, height = 100, метод должен вернуть строку Rectangle(5, 10, 50, 100).
# each class is initialized, but the base/parent one.
class GeometricShape :
    def to_string(self) :
        # extracting the name of the class
        name = self.__class__.__name__
        # extracting the list of attributes
        attrs = self.__dict__.values()
        return name + '(' + ', '.join(map(str, attrs)) + ')'


class Rectangle(GeometricShape) :
    def __init__(self, x, y, width, height) :
        self.x = x
        self.y = y
        self.width = width
        self.height = height


class Circle(GeometricShape) :
    def __init__(self, x, y, radius) :
        self.x = x
        self.y = y
        self.radius = radius


class Hexagon(GeometricShape) :
    def __init__(self, a, b, c, d, e, f, side_len) :
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f
        self.side_len = side_len


rect = Rectangle(5, 10, 50, 100)
print(rect.to_string())
circ = Circle(10, 15, 11)
print(circ.to_string())
hex = Hexagon(2, 4, 5, 7, 9, 10, 6)
print(hex.to_string())
