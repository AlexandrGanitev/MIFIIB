from cat_all_one_class import Cat, cats_list


# заработало при импортировании метода из основного класса Cat.cats_list словаря
def printing_the_list_of_pets(self) :
    for cat in cats_list :
        cat_obj = Cat()
        cat_obj.cats_from_dict(cat)
        print("Имя нашего питомца: ", cat_obj.name)
        print("Пол питомца: ", cat_obj.sex)
        print("Возраст питомца: ", cat_obj.age)

# это работает, но выдаёт следующую ошибку - AttributeError: type object 'Cat' has no attribute 'cats_list'
# for cat in Cat.cats_list :
#     cat_obj = Cat()
#     cat_obj.cats_from_dict(cat)
#     print("Имя нашего питомца: ", cat_obj.name)
#     print("Пол питомца: ", cat_obj.sex)
#     print("Возраст питомца: ", cat_obj.age)

# result = Cat()
# print(result)
# cat1 = Cat.data_cats(Cat)
# print(cat1)
