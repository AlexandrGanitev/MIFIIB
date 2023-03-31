# Python code to demonstrate how parent constructors
# are called.

# parent class
class Person(object) :

    # __init__ is known as the constructor
    def __init__(self, name, idnumber) :
        self.name = name
        self.idnumber = idnumber

    def display(self) :
        print(self.name)
        print(self.idnumber)


# child class
class Employee(Person) :
    def __init__(self, name, idnumber, salary, post) :
        self.salary = salary
        self.post = post

        # invoking the __init__ of the parent class
        # здесь мы передаём в родительский конструктор класса два аргумента, а дочерний (подкласс)
        # принимает 4 аргумента (обратить внимание)
        Person.__init__(self, name, idnumber)


# creation of an object variable or an instance. Четыре аргумента (!)
emp = Employee('Yurii', 886012, 200000, "Intern")

# calling a function of the class Person using its instance
emp.display()

print('*' * 25, "Didn't call the __init__ of the parent: ")
# Python program to demonstrate error if we forget to invoke __init__() of the parent
# If you forget to invoke the __init__() of the parent class then its instance variables would
# not be available to the child class.
#
# The following code produces an error for the same reason.

class A :
    def __init__(self, n='Rahul') :
        self.name = n


class B(A) :
    def __init__(self, roll) :
        self.roll = roll


object = B(23) # A класс не создан!
print(object.name)
