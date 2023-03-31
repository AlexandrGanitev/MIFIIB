class Test:
    def __init__(self):
        self.foo = 11
        self._bar = 23
        self.__baz = 23

t = Test()
# Without arguments, return the list of names in the current local scope. With an argument,
# attempt to return a list of valid attributes for that object.
print(dir(t))

# Let’s create another class that extends the Test class and attempts to override its existing
# attributes added in the constructor:
class ExtendedTest(Test):
    def __init__(self):
        super().__init__()
        self.foo = 'overridden'
        self._bar = 'overridden'
        self.__baz = 'overridden'

t2 = ExtendedTest()
print(dir(t2))
print(t2.foo)
print(t2._bar)
# print(t2.__baz) # This is the name mangling that the Python interpreter applies.
# It does this to protect the variable from getting overridden in subclasses.
print(t2._Test__baz) # But the original _Test__baz is also still around

class ManglingTest:
    def __init__(self):
        self.__mangled = 'hello'

    def get_mangled(self):
        return self.__mangled

# Does name mangling also apply to method names? It sure does—name mangling affects all names that
# start with two underscore characters (“dunders”) in a class context:
print(ManglingTest().get_mangled())
# >>> ManglingTest().get_mangled()
# 'hello'
# print(ManglingTest().__mangled)
# >>> ManglingTest().__mangled
# AttributeError: "'ManglingTest' object has no attribute '__mangled'"
class MangledMethod:
    def __method(self):
        return 42

    def call_it(self):
        return self.__method()

# MangledMethod().__method()
# >>> MangledMethod().__method()
# AttributeError: "'MangledMethod' object has no attribute '__method'"
print(MangledMethod().call_it())
# 42

_MangledGlobal__mangled = 23
# In this example I declared a global variable called _MangledGlobal__mangled. Then I accessed the
# variable inside the context of a class named MangledGlobal. Because of name mangling I was able
# to reference the _MangledGlobal__mangled global variable as just __mangled inside the test() method
# on the class.
class MangledGlobal:
    def test(self):
        return __mangled
print(MangledGlobal().test())
# >>> MangledGlobal().test()
# 23
# Perhaps surprisingly, name mangling is not applied if a name starts and ends with double underscores.
# Variables surrounded by a double underscore prefix and postfix are left unscathed by the Python interpeter:

class PrefixPostfixTest:
    def __init__(self):
        self.__bam__ = 42

print(PrefixPostfixTest().__bam__)
# >>> PrefixPostfixTest().__bam__
# 42
# However, names that have both leading and trailing double underscores are reserved for special use in the language.
# This rule covers things like __init__ for object constructors, or __call__ to make an object callable.

# Per convention, a single standalone underscore is sometimes used as a name to indicate that a
# variable is temporary or insignificant.
#
# For example, in the following loop we don’t need access to the running index and we can use “_” to
# indicate that it is just a temporary value:
#
for _ in range(32):
    print('Hello, World.')
print('*' * 25)
car = ('red', 'auto', 12, 3812.4)
color, _, _, mileage = car
#
print(color)
# 'red'
print(mileage)
# 3812.4
print(_)
# 12
print(car)