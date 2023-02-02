import numpy as np

"""Задані координати n точок на площині (x1,y1),...,(xn,yn). Знайти номери
двох точок, відстань між якими найбільша (вважати, що така пара точок
єдина), та саму відстань.
Використати масиви numpy. Точки розмістити у двовимірному масиві 2xn.
Побудувати тривимірний масив усіх можливих пар точок. Для побудови
використати індексні масиви. Описати векторизовану функцію, яка обчислює
відстань між 2 точками.
"""


def most_distance(pts):
    # print(pts)
    pts_shifted = np.roll(pts, 1, axis=2)  # посуваємо точки на 1 вправо, axis=2 - вісь на якій посуваємо
    # print(pts_shifted)
    dis = np.sqrt(np.sum((pts - pts_shifted)**2, axis=1))  # шукаємо відстань  між точками
    # print(dis)
    res = np.max(dis)
    # print(res)
    needed_values = pts[
        np.sqrt(np.sum((pts - pts_shifted)**2, axis=1)) == np.max(np.sqrt(np.sum((pts - pts_shifted)**2, axis=1)))
    ]
    # для отримання елементів, у яких виконується умова максимальної відстані
    return res, needed_values


def count_points(pts):
    n = pts.shape[1]  # кількість точок = кількість стовпчиків
    lst = []
    for i in range(n):
        for j in range(i + 1, n):
            lst.append(
                pts[:, np.array((i, j))]  # індексний масив
            )  # : - беремо по стовпчиках
    # будуємо тривимірний масив всіх можливих двійок елементів
    triplets = np.stack(lst)  # об'єднуємо елементи з колекції lst в один масив

    max_distance, values = most_distance(triplets)
    print(f"The largest distance between points is {max_distance}.")
    # print(values)
    # індекс елементу нашого масиву значення якого = values[0][0], values[0][1] в масиві х
    ind_x = np.where((x == values[0][0]) & (x == values[0][1]))
    ind_y1 = np.where((y == values[1][0]))
    ind_y2 = np.where((y == values[1][1]))
    print(f"Indexes of coordinate of first point: {(ind_x[0][0], ind_y1[0][0])}.")
    print(f"Indexes of coordinate of second point: {(ind_x[0][1], ind_y2[0][0])}.")


if __name__ == "__main__":
    x = np.array([-1, 1, 0, 0])
    y = np.array([0, 0, np.sqrt(9), -np.sqrt(3)])
    points = np.vstack((x, y))
    # print(points)
    count_points(points)

