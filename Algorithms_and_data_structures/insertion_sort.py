a = [4, 6, 7, 3, 2,52,34,123,22,0]


def insertion_sort(l):
    for idx, elementi in enumerate(l):
        temp = elementi
        for jdx, elementj in enumerate(l):
            if jdx == idx:
                break
            elif elementj > temp:
                l[jdx] = temp
                l[idx] = elementj
                temp = elementj
    return l


print(insertion_sort(a))
