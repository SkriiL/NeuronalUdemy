import numpy as np
import matplotlib.pyplot as plt


def f(a, x):
    return a * x


def j(a, x, y):
    return (y - a * x) ** 2


def j_ableitung_a(a, x, y):
    return -2 * x * (y - a * x)


point = (1, 4)

a = 1
rate = 0.05
for i in range(0, 50):
    da = j_ableitung_a(a, point[0], point[1])
    a -= rate * da
    print("Kosten wenn a =", a, ": ", j(a, point[0], point[1]))
    
xs = np.arange(-2, 2, 0.1)
ys = f(a, xs)
plt.plot(xs, ys)

plt.scatter(point[0], point[1])
plt.show()