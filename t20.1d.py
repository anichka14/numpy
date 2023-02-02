import numpy as np
import matplotlib.pyplot as plt


@np.vectorize
def f01(n):
    return ((2 * n ** 4 + n ** 3 + 1) ** (1/3) - n * (2 * n + 3) ** (1/3)) / (n + 1) ** (1 / 3)


def plot_function(x, y, b=None, eps=0.1):
    plt.figure(figsize=(9, 6))
    if b is None:
        plt.plot(x, y, ".m")
        return x[-1], y[-1]
    else:
        k = -1
        prev = False
        for i in range(x.size):
            if abs(y[i] - b) < eps:
                if prev is False:
                    prev = True
                    k = i
            else:
                prev = False
        if prev is False:
            return None, None

        begin = 0
        plt.plot(x[begin:], y[begin:], ".m")
        plt.plot(np.array([x[begin], x[-1]]), np.array([b, b]), '-g')
        plt.plot(np.array([x[begin], x[-1]]), np.array([b - eps, b - eps]), '-r')
        plt.plot(np.array([x[begin], x[-1]]), np.array([b + eps, b + eps]), '-r')
        plt.axis([x[begin], x[-1], b - 2 * eps, b + 2 * eps])
        return x[k], y[k]


if __name__ == "__main__":
    x = np.arange(1, 1000, 1)
    y = f01(x)
    b = -0.41956
    x0, y0 = plot_function(x, y, b, 0.01)
    print(x0, y0)
    plt.show()
