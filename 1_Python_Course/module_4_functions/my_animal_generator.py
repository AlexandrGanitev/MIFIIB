def my_animal_generator():
    yield 'корова'
    print('---')
    for animal in ['кот', 'собака', 'медведь']:
        yield animal
    print('---')
    yield 'кит'

a = my_animal_generator()
print(next(a))
# print('---') вызван не будет

print(next(a))

for i in a:
    print(i)