import datetime

# Помимо того, что классы служат фабрикой по производству однотипных объектов со сходным поведением,
# они имеют еще одну важную особенность — наследование.
#
# Как мы уже видели, объекты, созданные при помощи класса, наследуют атрибуты класса, которые
# объявлены прямо в теле, а не добавлены в конкретный независимый экземпляр. Помимо этого, классы
# сами по себе тоже умеют наследовать друг у друга не только атрибуты, но и методы.
#
# Это значит, что родительские атрибуты и методы будут доступны у так называемых дочерних
# (или производных) классов. Убедимся в этом. Чтобы задать родительский класс, надо указать
# его в скобках при объявлении класса, как будто это аргумент функции:


class Product1 :
    max_quantity = 100000

    def __init__(self, name, category, quantity_in_stock) :
        self.name = name
        self.category = category
        self.quantity_in_stock = quantity_in_stock

    def is_available(self) :
        return True if self.quantity_in_stock > 0 else False


class Food(Product1) :
    is_critical = True
    needs_to_be_refreshed = True
    refresh_frequency = datetime.timedelta(days=1)


# Мы создавали объект eggs как экземпляр класса Food, но при этом ему доступны как атрибуты родительского
# класса (max_quantity), так и его методы (is_available).
#
# Фактически получилось ещё интереснее: для создания экземпляра класса Food мы использовали конструктор
# его родительского класса — Product.
eggs = Food(name="eggs", category="food", quantity_in_stock=5)
print(eggs.max_quantity)
print(eggs.is_available())