# Задание 6.7.1.
# Откройте сайт "Дом питомца" и на основе имеющихся в нем данных создайте конструктор класса Cat со
# следующими параметрами: имя, пол, возраст.
#
# В отдельный файл импортируйте и создайте объект Cat, который выводит имеющихся на сайте котов,
# с одинаковыми параметрами, но с разными значениями.

# словарь с питомцами и их характеристиками
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


class Cat :
    def __init__(self, name="", sex="", age=0) :
        self.name = name
        self.sex = sex
        self.age = age

    def cats_from_dict(self, cats_dict) :
        self.name = cats_dict.get("name")
        self.sex = cats_dict.get("sex")
        self.age = cats_dict.get("age")
        # print(cats_dict)


# *********************** мои мытарства, наконец-то оформил создание объектов класса Cat из другого класса *****
    # def printing_the_list_of_pets(self) :
    #     for cat in cats_list :
    #         cat_obj = Cat()
    #         cat_obj.cats_from_dict(cat)
    #         print("Имя нашего питомца: ", cat_obj.name)
    #         print("Пол питомца: ", cat_obj.sex)
    #         print("Возраст питомца: ", cat_obj.age)

#
# for cat in cats_list :
#     cat_obj = Cat()
#     cat_obj.cats_from_dict(cat)
#     print("Имя нашего питомца: ", cat_obj.name)
#     print("Пол питомца: ", cat_obj.sex)
#     print("Возраст питомца: ", cat_obj.age)
