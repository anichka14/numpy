import numpy as np
import matplotlib.pyplot as plt


def taylor_sqrt(n):
    def _taylor_sqrt(x):
        s = 1
        p = 1
        for k in range(2, n + 1):
            p *= - x * (2 * k - 5) / (2 * k - 2)
            s += p
        return s
    _taylor_sqrt.__name__ = f"taylor_sqrt({n})"
    return _taylor_sqrt


def average_error(f1, f2, xmin, xmax, ymin, ymax):
    box_square = (xmax - xmin) * (ymax - ymin)
    count = int(box_square * 1000)
    x = np.random.uniform(xmin, xmax, count)
    y = np.random.uniform(ymin, ymax, count)
    y1 = f1(x + 1)
    y2 = f2(x)
    count_in = np.sum(
        np.logical_or(
            np.logical_and(y1 < y, y < y2),
            np.logical_and(y2 < y, y < y1)
        )
    )
    square = count_in / count * box_square
    return np.sqrt(square / box_square)


def move_axes():
    a0, b0, c0, d0 = plt.axis()
    d0 = 3 / 4 * (b0 - a0)
    c0 = -d0 / 2
    plt.axis((a0, b0, c0, d0))
    ax = plt.gca()
    ax.spines["top"].set_color("none")
    ax.spines["right"].set_color("none")
    ax.spines["bottom"].set_position(("data", 0))
    ax.spines["left"].set_position(("data", 0))
    ax.xaxis.set_ticks_position("bottom")
    ax.yaxis.set_ticks_position("left")

    plt.legend(loc="best")


def plot_f1f2(x, f1, f2):
    y1 = f1(x + 1)
    y2 = f2(x)
    plt.plot(x, y1, "-m", lw=2, label=f1.__name__)
    plt.plot(x, y2, "-b", lw=2, label=f2.__name__)
    plt.fill_between(x, y1, y2, facecolor="green")

    error = average_error(f1, f2, *plt.axis())
    print(error)

    move_axes()


def plot_diff(x, f1, f2):
    y = abs(f2(x) - f1(x + 1))
    plt.plot(x, y, "-r", lw=2)
    plt.fill_between(x, y, facecolor="yellow", label="difference")

    move_axes()


def plot_functions(a, b, interpolated, interpolator):
    plt.figure(figsize=((b - a) * 3, 4 * (b - a)))
    x = np.linspace(a, b, int(b - a) * 50)
    plt.subplot(2, 1, 1)
    plot_f1f2(x, interpolated, interpolator)
    plt.subplot(2, 1, 2)
    plot_diff(x, interpolated, interpolator)

    plt.show()


if __name__ == "__main__":
    a = -1
    b = 1
    m = 3
    plot_functions(
        a, b,
        np.sqrt,
        taylor_sqrt(m)
    )
