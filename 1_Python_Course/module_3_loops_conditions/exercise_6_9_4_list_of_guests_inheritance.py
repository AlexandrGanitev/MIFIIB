# Задание 6.9.4
# Команда проекта «Дом питомца» планирует большой корпоратив для своих волонтеров.
# Вам необходимо написать программу, которая позволяла бы составлять список нескольких гостей.
# Решите задачу с помощью метода конструктора и примените один из принципов наследования.
#
# При выводе в консоль вы должны получить:  “Иван Петров, г.Москва, статус "Наставник"

class Person(object) :

    # Constructor
    def __init__(self, name) :
        self.name = name

    # To check if this person is an employee
    def get_name(self) :
        return self.name


class Volonteers(Person) :
    def __init__(self, name, city, position) :
        Person.__init__(self, name)
        self.city = city
        self.position = position

    def get_city(self) :
        return self.city

    def get_position(self) :
        return self.position


# Создаём объект класса Volonteers
guest = Volonteers("Иван Петров", "Москва", "Наставник")  # создаем нового волонтёра
guest_name = guest.get_name()
guest.city = guest.get_city()
guest.position = guest.get_position()

print(f'{guest_name}, г. {guest.city}, статус "{guest.position}"')
