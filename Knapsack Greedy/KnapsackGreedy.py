def knapsackGreedy(value, weight, capacity):
    index = list(range(len(value)))
    ratio = [v/w for v, w in zip(value, weight)]
    index.sort(key=lambda i: ratio[i], reverse=True)
    print(index)

    total_value = 0
    fractions = [0]*len(value)
    for i in index:
        if weight[i] <= capacity:
            fractions[i] = 1
            total_value += value[i]
            capacity -= weight[i]
        else:
            fractions[i] = capacity/weight[i]
            total_value += value[i]*capacity/weight[i]
            break

    print('Total Value:', total_value)
    print('Fractions:', fractions)


value = [18, 45, 21, 9, 30, 52, 15]
weight = [1, 5, 7, 1, 2, 4, 3]
capacity = 15

knapsackGreedy(value, weight, capacity)
