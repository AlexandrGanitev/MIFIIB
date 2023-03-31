# Scopes and Namespaces Example
# This is an example demonstrating how to reference the different scopes and namespaces,
# and how global and nonlocal affect variable binding:

def scope_test() :
    def do_local() :
        spam = "local spam"

    def do_nonlocal() :
        nonlocal spam
        spam = "nonlocal spam"

    def do_global() :
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)


scope_test()
print("In global scope:", spam)
# The output of the example code is:
#
# After local assignment: test spam
# After nonlocal assignment: nonlocal spam
# After global assignment: nonlocal spam
# In global scope: global spam

# Note how the local assignment (which is default) didn’t change scope_test's binding of spam.
# The nonlocal assignment changed scope_test's binding of spam, and the global assignment changed
# the module-level binding, i.e. beyond the scope of scope_test() module
print('*' * 25, 'Instance Objects example')


# Now what can we do with instance objects? The only operations understood by instance objects are attribute
# references. There are two kinds of valid attribute names: data attributes and methods.
#
# data attributes correspond to “instance variables” in Smalltalk, and to “data members” in C++.
# Data attributes need not be declared; like local variables, they spring into existence when they
# are first assigned to. For example, if x is the instance of MyClass created above, the following
# piece of code will print the value 16, without leaving a trace:
class Complex :
    def __init__(self, realpart, imagpart) :
        self.r = realpart
        self.i = imagpart


x = Complex(3.0, -4.5)
x.counter = 1
while x.counter < 10 :
    x.counter = x.counter * 2
print(x.counter)
del x.counter
