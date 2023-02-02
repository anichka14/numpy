import numpy as np

""" Скласти програму пошуку найменшого серед найбільших елементів
рядків квадратної дійсної матриці порядку n.
Використати масиви numpy та векторизувати програмний код."""


def min_max_v1(a):
    n = a.shape[0]
    max_lst = []
    for i in range(n):
        max_el = a[0][0]
        for j in range(n):
            if a[i][j] > max_el:
                max_el = a[i][j]
        max_lst.append(max_el)
    return min(max_lst)


def min_max_v2(a):
    return np.min(np.max(a, axis=1))


if __name__ == "__main__":
    a = np.array(
        [
                 [1, 8, 0],
                 [4, 5, 3],
                 [7, -8, 10]
        ]
    )
    print(min_max_v1(a))
    print(min_max_v2(a))
