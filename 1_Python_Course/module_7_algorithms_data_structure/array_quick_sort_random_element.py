import random
# random.choice(array[idx_left: idx_right])
array = [2, 3, 1, 4, 6, 5, 9, 8, 7]


def qsort_random(array, left, right, count=0) :
    p = random.choice(array[left :right + 1])
    i, j = left, right
    while i <= j :
        while array[i] < p :
            i += 1
        while array[j] > p :
            j -= 1
        if i <= j :
            count += 1
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1

    if j > left :
        qsort_random(array, left, j)
    if right > i :
        qsort_random(array, i, right)


qsort_random(array, 0, len(array) - 1) # наши три аргумента, сам массив, его первый и последний элементы
print(array)