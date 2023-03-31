# Важно! Если мы назовем атрибут или метод так же, как он называется в родительском классе,
# он будет переопределен!
class Event2 :
    def __init__(self, timestamp=0, event_type="", session_id="") :
        self.timestamp = timestamp
        self.type = event_type
        self.session_id = session_id

    def init_from_dict(self, event_dict) :
        self.timestamp = event_dict.get("timestamp")
        self.type = event_dict.get("type")
        self.session_id = event_dict.get("session_id")

    def show_description(self) :
        print("This is generic event.")


class ItemViewEvent(Event2) :
    type = "itemViewEvent"

    def __init__(self, timestamp=0, session_id="", number_of_views=0) :
        self.timestamp = timestamp
        self.session_id = session_id
        self.number_of_views = number_of_views

    def show_description(self) :
        print("This event means someone has browsed an item.")


if __name__ == "__main__" :
    test_view_event = ItemViewEvent(timestamp=1549461608000, session_id="0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
                                    number_of_views=6)
    test_view_event.show_description()
    print(test_view_event.type)


# __name__ in Python
# Python's __name__ special variable stores the name of the currently running Python script or module.
# The Python __name__ variable was added in Python 3.0 and is not present in Python 2.x. When a Python
# script or module is being executed, the __name__ variable is given the value __main__ for the present
# Python script or module.
#
# What does _name_ mean ?
# Python has a built-in variable called __name__ that records the name of the currently running module
# or script. The __name__ variable merely holds the name of the module or script unless the current module
# is executing, in which case the value __main__ is set to it.
#
# Therefore, if a Python script is imported into another Python script, its __name__ variable should
# always have the value __main__ when that Python script is running. Otherwise, it would have the name
# of the module.
#
# Example :
# To further understand this, let's use an example. Make a script in Python called testing.py,
# and append the following code to it :
#
# # Code to define a function
def anything() :
    print('Value of the __name__ : ', __name__)


anything()

# Что получили:
#
# Переопределили конструктор класса. Теперь мы используем не родительский, а свой, и передаём в него другой
# набор аргументов. Так у нас получился кастомизированный набор атрибутов: у родительского класса
# нет атрибута number_of_views.

# Переопределили значение атрибута type с помощью атрибута класса. Теперь при вызове type от экземпляра
# нашего дочернего класса мы получим значение атрибута type нашего класса ItemViewEvent.

# Переопределили работу метода show_description: теперь он показывает более специфичное для класса описание.
