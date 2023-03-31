# Polymorphism with a Function and objects:
#
# It is also possible to create a function that can take any object, allowing for polymorphism. In this example,
# let’s create a function called “func()” which will take an object which we will name “obj”. Though we are using
# the name ‘obj’, any instantiated object will be able to be called into this function. Next, let’s give the function
# something to do that uses the ‘obj’ object we passed to it. In this case, let’s call the three methods, viz.,
# capital(), language() and type(), each of which is defined in the two classes ‘India’ and ‘USA’. Next, let’s
# create instantiations of both the ‘India’ and ‘USA’ classes if we don’t have them already. With those, we can
# call their action using the same func() function:


class Russia() :
    def capital(self) :
        print("Moscow is the capital of Russia.")

    def language(self) :
        print("Russian is the most widely spoken language of Russia.")

    def type(self) :
        print("Russia is a God's civilization.")


class USA() :
    def capital(self) :
        print("Washington, D.C. is the capital of USA.")

    def language(self) :
        print("English is the primary language of USA.")

    def type(self) :
        print("USA is a developed country.")


def func(obj) :
    obj.capital()
    obj.language()
    obj.type()


obj_rus = Russia()
obj_usa = USA()

func(obj_rus)
func(obj_usa)

print('*' * 25, 'Другой пример')


class Tomato() :
    def type(self) :
        print("Vegetable")

    def color(self) :
        print("Red")


class Apple() :
    def type(self) :
        print("Fruit")

    def color(self) :
        print("Red")


def func(obj) :
    obj.type()
    obj.color()


obj_tomato = Tomato()
obj_apple = Apple()
func(obj_tomato)
func(obj_apple)
