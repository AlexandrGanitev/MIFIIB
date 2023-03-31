# Вместо такого явного разбора словаря в цикле мы могли бы задать нашему классу метод,
# который позволяет инициализировать наш объект напрямую. Для этого давайте поправим объявление
# нашего класса и зададим для каждой переменной её значение по умолчанию, чтобы мы могли
# инициализировать объект без заполнения. Это делается с помощью указания значений по
# умолчанию сразу после названия аргумента:

class Event1 :
    def __init__(self, timestamp=0, event_type="", session_id="") :
        self.timestamp = timestamp
        self.type = event_type
        self.session_id = session_id

    # Отлично, а теперь добавим метод. Не забываем, что метод принимает на вход self первым аргументом.
    # Метод идет с отступом и должен быть объявлен внутри класса
    def init_from_dict(self, event_dict) :
        self.timestamp = event_dict.get("timestamp")
        self.type = event_dict.get("type")
        self.session_id = event_dict.get("session_id")
        # print(event_dict) # печатает словарь


events = [
    {
        "timestamp" : 1554583508000,
        "type" : "itemViewEvent",
        "session_id" : "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
    },
    {
        "timestamp" : 1555296337000,
        "type" : "itemViewEvent",
        "session_id" : "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
    },
    {
        "timestamp" : 1549461608000,
        "type" : "itemBuyEvent",
        "session_id" : "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
    },
]


for event in events :
    event_obj = Event1()
    event_obj.init_from_dict(event)
    print(event_obj.timestamp)
