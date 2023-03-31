abons = {"Иванов", "Петров", "Васильев", "Антонов"}

debtors = {"Петров", "Антонов"}
print("Два множества: ", abons, debtors)
non_debtors = abons.difference(debtors)

print("Разница между множествами:", non_debtors)
# {'Васильев', 'Иванов'}
print("Симметричная разность:", abons.symmetric_difference(debtors))