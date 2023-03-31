class Event :
    def __init__(self, timestamp, event_type, session_id) :
        self.timestamp = timestamp
        self.type = event_type
        self.session_id = session_id


# the list of dictionaries
# Допустим, мы уже распарсили наши логи и получили список словарей вроде такого:
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

# Давайте для каждого события в списке создадим соответствующий ему объект с помощью конструктора,
# как мы уже делали. А чтобы убедиться, что объект создаётся, выведем на печать какой-нибудь из атрибутов:
# get() - получение значения ключа словаря
for event in events :
    event_obj = Event(timestamp=event.get("timestamp"),
                      event_type=event.get("type"),
                      session_id=event.get("session_id"))
    print(event_obj.timestamp, event_obj.session_id, event_obj.type)
# думал, почему выше не работает (unresolved) event_type, ведь мы пишем event_type=event.get("type").
# надо посмотреть сюда, на конструктор класса:
#     def __init__(self, timestamp, event_type, session_id) :
#         self.timestamp = timestamp
#         self.type = event_type
#         self.session_id = session_id
# event_type это аргумент, а переменная (что мы пытаемся распечатать) - type!
