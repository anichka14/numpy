import numpy as np
import random

"""У капелюсі є m*k кульок: по k кульок m кольорів (m > 1). За один раз
витягають d кульок (1 < d <= k). Яка ймовірність того, що всі вони одного
кольору?
Розв’язати задачу методом Монте-Карло з використанням масивів numpy.
Векторизувати програмний код, наскільки можливо."""

TEST_NUM = 10000
m = random.randint(2, 10)  # кількість кольорів
colors = np.arange(m)  # масив кольорів
k = random.randint(2, 10)  # кількість кульок одного кольору
d = random.randint(2, k)  # кількість кульок, які ми дістаємо


def check(choice):
    res = np.zeros(TEST_NUM, dtype=bool)
    for i in range(TEST_NUM):
        if np.all(choice[i] == choice[i][0]):  # перевіряємо, щоб всі значення в рядку були однакові
            # чи всі значення в рядку еквівалентні першому значенню рядка
            print(choice[i])
            res[i] = True
            # print(res[i])
    return res


def beads_probability(beads, count):
    # beads - можливі варіанти кульок
    # count - кількість кулок, які ми витягаємо за один раз
    # to_extract - те, що ми хочемо отримати
    choice = np.zeros((TEST_NUM, count), dtype=int)
    for i in range(TEST_NUM):
        choice[i, :] = np.random.choice(beads, count, replace=False)
    choice.sort(axis=1)  # сортуємо по рядкам
    print(choice)
    res = check(choice)
    return np.sum(res) / TEST_NUM


if __name__ == "__main__":
    hat = np.random.choice(colors, m * k)
    p = beads_probability(hat, d)
    print(f"{p * 100:.2f}%")
    print(f"Загальна кількість куль: {m * k}")
    print(f"Кількість кольорів: {m}")
    print(f"Кількість кульок одного кольру: {k}")
    print(f"Масив кольорів: {colors}")
    print(f"Кількість кульок, яку витягли за один раз: {d}")
