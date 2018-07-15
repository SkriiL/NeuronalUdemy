import numpy as np
import matplotlib.pyplot as plt


def f(a, x):
    return a * x


def j(a, x, y):
    return np.mean((y - a * x) ** 2)


def j_ableitung_a(a, x, y):
    return np.mean(-2 * x * (y - a * x))


points = np.array([
    [1, 4],
    [1.5, 5],
    [2, 8],
    [0.5, 3]
])

a = 1
rate = 0.05
for i in range(0, 50):
    da = j_ableitung_a(a, points[:, 0], points[:, 1])

    a -= rate * da
    cost = j(a, points[:, 0], points[:, 1])
    print("Kosten wenn a =", a, ": ", cost)

xs = np.arange(-2, 2, 0.1)
ys = f(a, xs)
plt.plot(xs, ys)

plt.scatter(points[:, 0], points[:, 1], color="red")
plt.show()