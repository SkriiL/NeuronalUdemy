import numpy as np
import matplotlib.pyplot as plt

points = np.array([
    [20, 1],
    [17, 0],
    [15, 0],
    [10, 0],
    [30, 1],
    [40, 1],
    [35, 1],
    [13, 0],
    [5, 0],
    [19, 1],
    [25, 1],
    [8, 0],
])


def s(x):
    return 1 / (1 + np.exp(-x))


def f(a, b, x):
    return s(a * x + b)


def j(a, b, x, y):
    return -np.mean(y * np.log(f(a, b, x)) + (1 - y) * np.log(1 - f(a, b, x)))


def j_ableitung_a(a, b, x, y):
    return np.mean(x * (s(a * x + b) - y))


def j_ableitung_b(a, b, x, y):
    return np.mean(s(a * x + b) - y)


a = 1
b = 1
rate = 0.05
for i in range(0, 15000):
    da = j_ableitung_a(a, b, points[:, 0], points[:, 1])
    db = j_ableitung_b(a, b, points[:, 0], points[:, 1])

    a -= rate * da
    b -= rate * db
    cost = j(a, b, points[:, 0], points[:, 1])
    print("Kosten wenn a =", a, "und b=", b, ": ", cost)


xs = np.arange(1, 60, 0.5)
ys = f(a, b, xs)
plt.plot(xs, ys)


plt.scatter(points[:, 0], points[:, 1])
plt.show()

print("---------------------------------------------------------")
print(f(a, b, 16))