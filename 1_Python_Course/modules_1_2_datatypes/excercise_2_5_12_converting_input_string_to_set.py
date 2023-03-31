# Задание 2.5.12
# Напишите программу, которая на вход принимает текст и выводит количество уникальных символов.
text_input = input("Введите ваш текст: ")
entered_text = list(set(text_input))
print(entered_text)
print("Количество уникальных символов: ", len(entered_text))