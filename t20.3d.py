import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def f01(x, n):  # функція приймає розбиття (масив х), n - кількість доданків в частковій сумі ряду Тейлора
    s = 1
    p = 1
    for k in range(1, n + 1):
        p *= x / k
        s += p
    return s


# виділяємо відрізок, де ми будемо робити анімацію
# значення а, b будемо дивитися як окіл точки 0 і в залежності від ф-ції, яку ми збираємось розкладати
a = -1
b = 1
m = 20  # m - це кількість кадрів (в нашому випадку це максимальна к-ть доданків ряду)


x = np.linspace(a, b, int((b - a) * 100))  # розбиття відрізка [a, b], к-ть частин залежить від довжини (b - a)
fig = plt.figure()  # посилання на графік для анімації
plt.axis([a, b, 0, 3/4 * (b - a)])
# a, b - межі для х, -3/8 * (b - a), 3/8 * (b - a) - для у (у відношенні 3 : 4)
line, = plt.plot([], [], "-g", lw=2)  # повертає посилання на лінію, яку вона будує
# [], [] - будуємо пустий графік


def init():  # викликається 1 раз на початку анімації
    plt.plot(x, np.exp(x), "--m", lw=5)
    return line,


def animate(i):  # змінює координати лінії
    y = f01(x, i + 1)
    line.set_data(x, y)
    return line,


anim = FuncAnimation(
    fig,
    animate,
    init_func=init,
    frames=m,
    interval=500,
    repeat=False
)
plt.show()
anim.save("func.gif", writer="pillow")
