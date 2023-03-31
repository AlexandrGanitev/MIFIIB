# Python example to show the working of multiple
# inheritance

class Base1(object) :
    def __init__(self) :
        self.str1 = "Geek1"
        print("Base1 объект создан")


class Base2(object) :
    def __init__(self) :
        self.str2 = "Geek2"
        print("Base2 объект создан")


class Derived(Base1, Base2) :
    def __init__(self) :
        # Calling constructors of Base1 and Base2 classes
        Base1.__init__(self)
        Base2.__init__(self)
        print("Derived объект создан только после создания базовых классов")

    def printStrs(self) :
        print(self.str1, self.str2)


# Первое - создаём объект производного класса из Base1, Base2
obj = Derived()
obj.printStrs()

