# Посчитайте количество сравнений, которые производятся в алгоритме выбором из примера.
array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
count_comparison = 0
for i in range(len(array)) :  # проходим по всему массиву
    idx_min = i  # сохраняем индекс предположительно минимального элемента
    for j in range(i, len(array)) :
        count_comparison += 1
        if array[j] < array[idx_min]:
            idx_min = j
    if i != idx_min :  # если индекс не совпадает с минимальным, меняем
        array[i], array[idx_min] = array[idx_min], array[i] # перемена мест позиционных перемменых,
        # array[i], array[idx_min] меняются местами

print("Сортированный массив: ", array)
print("Число сравнений", count_comparison)
