import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler


def f(a, b, x):
    return a * x + b


def j(a, b, x, y):
    return np.mean((y - (a * x + b)) ** 2)


def j_ableitung_a(a, b, x, y):
    return np.mean(-2 * x * (-a * x - b + y))


def j_ableitung_b(a, b, x, y):
    return np.mean(-2 * (-a * x - b + y))



df = pd.read_csv("autos_prepared.csv")

points = df[["kilometer", "price"]].values
s = StandardScaler()
points = s.fit_transform(points)

a = 1
b = 1
rate = 0.005
for i in range(0, 500):
    da = j_ableitung_a(a, b, points[:, 0], points[:, 1])
    db = j_ableitung_b(a, b, points[:, 0], points[:, 1])

    a -= rate * da
    b -= rate * db
    cost = j(a, b, points[:, 0], points[:, 1])
    print("Kosten wenn a =", a, "und b=", b, ": ", cost)

xs = np.arange(-2.1, 2, 0.5)
ys = f(a, b, xs)
plt.plot(xs, ys)

plt.scatter(points[:, 0], points[:, 1])
plt.show()