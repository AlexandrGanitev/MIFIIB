import json

with open('json_example.json', encoding='utf8') as f:
    strfile = f.read() # эта переменная просто строка
    templates = json.loads(strfile) # loads() переводит содержимое в словарь
    # load() считывает файл, loads() строку

print(templates)
print(type(templates))