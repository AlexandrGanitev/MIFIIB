# Задание 6.10.5
# Задание на самопроверку.
#
# Создать класс SquareException. Добавить в конструктор класса Square собственное исключение
# NonPositiveDigitException, унаследованное от ValueError, которое будет срабатывать каждый раз,
# когда сторона квадрата меньше или равна 0.


class Square:
    def __init__(self, a) :
        self.a = a
        if a < 0:
            raise NonPositiveDigitException('Неправильно указанна сторона квадрата')

    def get_area_square(self) :
        return self.a ** 2


class NonPositiveDigitException(ValueError) :
    pass


square_side = int(input("Введите сторону квадрата: "))


new_square = Square(square_side)
print(new_square.get_area_square())
