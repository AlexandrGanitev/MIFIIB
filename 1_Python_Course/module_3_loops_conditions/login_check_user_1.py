# Допишите функцию check_user так, чтобы она по логину пользователя
# проверяла, существует он или нет,
# после чего с помощью вложенного условия проверяла
# правильность пароля этого пользователя.
# Функция должна возвращать только True или False.
# Чтобы вернуть True, напишите "return True";
# чтобы вернуть False, напишите "return False".
login_list = ['user', 'iseedeadpeople', 'hesoyam']
user_database = {
    'user': 'password',
    'iseedeadpeople': 'greedisgood',
    'hesoyam': 'tgm'
}

def check_user(user, password):
    if user in login_list:
        print(f"Пользователь {user} вводит пароль...")
        if user_database[user] == password:
            return "Пользователь вошел в систему"
        else:
            return "Неверный пароль!"
    else:
        return "Несуществующий пользователь"
# Когда я использовал print вместо return (а return это функция и она должна вернуть результат,
# и тогда, после каждой строки выведенного текста, программа добавляла None. Заменил на должное return.

print(check_user('hopa', 'mopa'))
print(check_user('hesoyam', 'tgm'))
print(check_user('iseedeadpeople', 'asd'))
