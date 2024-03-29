class Rectangle :
    def __init__(self, a, b) :
        self.a = a
        self.b = b

    def get_area(self) :
        return self.a * self.b


class Square :
    def __init__(self, a) :
        self.a = a

    def get_area_square(self) :
        return self.a ** 2


class Circle :
    def __init__(self, radius) :
        self.radius = radius

    def get_area_circle(self) :
        return 3.14 * self.radius ** 2
