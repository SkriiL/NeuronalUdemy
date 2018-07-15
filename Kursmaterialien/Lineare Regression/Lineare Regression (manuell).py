import numpy as np
import matplotlib.pyplot as plt


def f(a, x):
    return a * x


def J(a, x, y):
    return (y - a * x) ** 2


def J_ableitung_a(a, x, y):
    return -2 * x * (y - a * x)


point = (1, 4)
lr = 0.05
a = 1
for i in range(0, 50):
    da = J_ableitung_a(a, point[0], point[1])
    a = a - lr * da
    print(a)
    print("Kosten wenn a = " + str(a) + ": " + str(J(a, point[0], point[1])))

xs = np.arange(-2, 2, 0.1)
ys = f(a, xs)
plt.plot(xs, ys)

plt.scatter(point[0], point[1])
plt.show()

