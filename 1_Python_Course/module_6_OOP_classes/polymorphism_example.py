# The below code shows how Python can use two different class types, in the same way.
# We create a for loop that iterates through a tuple of objects. Then call the methods
# without being concerned about which class type each object is. We assume that these
# methods actually exist in each class.

#  NOTE! - Don't use parentheses unless you are subclassing other classes!
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


# Создаём объекты наших двух классов
obj_rus = Russia()
obj_usa = USA()

for country in (obj_rus, obj_usa) :
    country.capital()
    country.language()
    country.type()
