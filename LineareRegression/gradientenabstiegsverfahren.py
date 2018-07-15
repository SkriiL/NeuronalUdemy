import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return 0.1 * x ** 4 - 0.2 * x ** 2 + 5 * x ** 3 + x


def f_ableitung(x):
    return 0.4 * x ** 3 - 0.4 * x + 15 * x ** 2 + 1


x = 5
rate = 0.01
plt.scatter(x, f(x), c="r")
for i in range(0, 25):
    steigung_x = f_ableitung(x)
    x -= rate * steigung_x
    plt.scatter(x, f(x), c="r")
    print(x, f_ableitung(x))

xs = np.arange(-6, 6, 0.1)
ys = f(xs)
plt.plot(xs, ys)
plt.show()