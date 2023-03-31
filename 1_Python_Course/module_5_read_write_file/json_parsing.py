import json

with open('json_example.json', encoding='utf8') as f :
    templates = json.load(f)

print(templates)
print(type(templates))
