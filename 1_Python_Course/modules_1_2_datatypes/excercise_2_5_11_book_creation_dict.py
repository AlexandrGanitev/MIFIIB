"""
Skillfactory | Задача по Python
Напишите программу, которая получает на вход название книги - title,
фамилию автора - author и год выпуска - year.
Полученные данные должны быть преобразованы в словарь book с ключами:
title, author, year. Причем year нужно преобраовать в тип int.
"""
# Введите свое решение ниже
title = input("Введите название книги:")
author = input("Введите фамилию автора:")
year = int(input("Введите год выпуска:"))

# book = {}
book = {"title": title,
        "author": author,
        "year":year}

print(book)