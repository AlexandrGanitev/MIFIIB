# Задание 6.7.1.
# Откройте сайт "Дом питомца" и на основе имеющихся в нем данных создайте конструктор класса Cat со
# следующими параметрами: имя, пол, возраст.
#
# В отдельный файл импортируйте и создайте объект Cat, который выводит имеющихся на сайте котов,
# с одинаковыми параметрами, но с разными значениями.

class Cat :
    def __init__(self, name, sex, age) :
        self.name = name
        self.sex = sex
        self.age = age


cats_list = [
    {
        "name" : "Семён",
        "type" : "кошка",
        "sex" : "мальчик",
        "breed" : "сибирская кошка",
        "age" : "2",
        "registration_number" : "с07032020",
        "status" : "не приютили"
    },
    {
        "name" : "Жора",
        "type" : "кошка",
        "sex" : "мальчик",
        "breed" : "сибирская кошка",
        "age" : "3",
        "registration_number" : "с07032023",
        "status" : "не приютили"
    },
    {
        "name" : "Кися",
        "type" : "кошка",
        "sex" : "девочка",
        "breed" : "ангорская кошка",
        "age" : "1",
        "registration_number" : "с07032110",
        "status" : "приютили"
    },
    {
        "name" : "Бася",
        "type" : "кошка",
        "sex" : "девочка",
        "breed" : "ангорская кошка",
        "age" : "1",
        "registration_number" : "с07032116",
        "status" : "приютили"
    }
]

for cat in cats_list :
    cat_obj = Cat(name=cat.get("name"),
                  sex=cat.get("sex"),
                  age=cat.get("age"))
    print(cat_obj.name, cat_obj.sex, cat_obj.age)

