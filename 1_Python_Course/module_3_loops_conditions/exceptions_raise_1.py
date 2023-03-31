try :
    age = int(input("How old are you?"))

    if age > 100 or age <= 0 :
        raise ValueError("Тебе не может быть столько лет")
except ValueError :
    print("Неправильный возраст")

print(f"You are {age} years old!")  # Возраст выводится только в случае, если пользователь ввёл правильный возраст.
