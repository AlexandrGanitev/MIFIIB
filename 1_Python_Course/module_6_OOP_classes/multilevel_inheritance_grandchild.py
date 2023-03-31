# A Python program to demonstrate inheritance

# Base or Super class. Note object in bracket.
# (Generally, object is made ancestor of all classes)
# In Python 3.x "class Person" is
# equivalent to "class Person(object)"

class Base(object) :

    # Constructor
    def __init__(self, name) :
        self.name = name

    # To get the name
    def getName(self) :
        return self.name


# Inherited or Sub class (Note Person in bracket)
class Child(Base) :

    # Constructor
    def __init__(self, name, age) :
        Base.__init__(self, name)
        self.age = age

    def getAge(self) :
        return self.age


# Inherited or Sub class (Note Person in bracket)


class GrandChild(Child) :

    def __init__(self, name, age, address) :
        Child.__init__(self, name, age)
        self.address = address

    # To get the address
    def getAddress(self) :
        return self.address


# Driver code
grn_chld = GrandChild("Lev", 23, "Lipetzk")
print(grn_chld.getName(), grn_chld.getAge(), grn_chld.getAddress())

