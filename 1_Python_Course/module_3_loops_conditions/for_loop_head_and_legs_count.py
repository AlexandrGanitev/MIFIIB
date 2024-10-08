"""
Рассмотрим следующую задачу. В клетке находятся фазаны и кролики.
Известно, что у них 35 голов и 94 ноги. Узнайте число фазанов и число кроликов.

Количество фазанов и кроликов выражается целым числом, поэтому будем перебирать
все возможные комбинации количества кроликов и фазанов, и если суммарное количество
их ног равно указанному в условии, то мы нашли одно из решений.
"""
heads = 35  # количество голов
legs = 94  # количество ног
print("Количество голов и ног:", heads, legs)
for r in range(heads + 1):  # количество кроликов
    # print(r)
    for ph in range(heads + 1):  # количество фазанов
        #  если суммарное количество голов превышено или ног превышено, то переходим на следующий шаг цикла
        if (r + ph) > heads or \
                (r * 4 + ph * 2) > legs:
            continue
        if (r + ph) == heads and (r * 4 + ph * 2) == legs:
            print("Количество кроликов", r)
            print("Количество фазанов", ph)
            print("---")
