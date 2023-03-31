import random


# ХОРОШАЯ ФУНКЦИЯ
# - имеет читаемое название, нужную информацию получает в аргументах
# - короткая/читаемая
# - возвращает результат (NO PRINT)
# - независимая (NO GLOBAL!!!), и не меняет ничего вне себя
# - умеет что-то делать одно, но умеет это хорошо и знает все для этого
# - если меняет пришедший аргумент, то возвращает None
# - тестируема!
# - https://www.youtube.com/watch?v=tY3i_MUvwgk&ab_channel=PythonRussian

def generate_pin(length: int) -> str:
    return ''.join(str(random.randint(0, 9)) for _ in range(length))


# этот вариант самый лучший, когда пришедший аргумент не меняется в функции
# используем return None, как флаг для пользователя, что мы собираемся что-го менять
# во входящем аргументе (здесь список)
def replace_fives(a_list: list, value: str) -> list[str]:
    return [element.replace('5', value) for element in a_list]


# если нужно поменять входящий список (a_list), словарь и т.д., то надо возвращатъ None:
# def replace_fives_inplace(a_list: list, value: str) :
#     for index in range(len(a_list)) :
#         a_list[index] = a_list[index].replace('5', value)


def write_file(filename: str, data: str) :
    with open(filename, 'w') as file :
        file.write(data)


# здесь нет глобальнх переменнх, мы вводим данных посредством аргументов
# pins_without_fives = replace_fives(pins, '6'), при необходимости, мы можем заменить '6' на любой символ

if __name__ == '__main__':
    pins = [generate_pin(8) for _ in range(9)]
    pins_without_fives = replace_fives(pins, '6')
    str_list = '\n'.join(pins_without_fives)
    print(pins_without_fives)
    write_file('test.txt', str_list)
