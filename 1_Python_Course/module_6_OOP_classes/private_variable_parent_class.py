# Python program to demonstrate private members
# of the parent class


class C(object) :
    def __init__(self) :
        self.c = 21

        # d is private instance variable
        self.__d = 42
# Since ‘d’ is made private by those underscores, it is not available to the child class ‘D’ and hence the error.
# __d означает частную переменную

class D(C) :
    def __init__(self) :
        self.e = 84
        C.__init__(self)


object1 = D()

# produces an error as d is private instance variable
print(object1.d)
