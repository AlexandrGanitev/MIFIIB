# Задание 17.5.1
# Задание на самопроверку.
#
# Представьте эту часть схемы в виде графа и создайте список смежности, используя словарь.

G = {"Адмиралтейская" :
         ["Садовая"],
     "Садовая" :
         ["Сенная площадь",
          "Спасская",
          "Адмиралтейская",
          "Звенигородская"],
     "Сенная площадь" :
         ["Садовая",
          "Спасская"],
     "Спасская" :
         ["Садовая",
          "Сенная площадь",
          "Достоевская"],
     "Звенигородская" :
         ["Пушкинская",
          "Садовая"],
     "Пушкинская" :
         ["Звенигородская",
          "Владимирская"],
     "Владимирская" :
         ["Достоевская",
          "Пушкинская"],
     "Достоевская" :
         ["Владимирская",
          "Спасская"]}

print(G)