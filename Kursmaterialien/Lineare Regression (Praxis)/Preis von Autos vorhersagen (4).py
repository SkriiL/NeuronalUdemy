import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

# Praxisbeispiel: Preis von Autos bestimmen!
#   -> Partielle Ableitung
#   -> Bias

df = pd.read_csv("./autos_prepared.csv")

points = df[["kilometer", "price"]].values
print(points)

def f(a, b, x):
    return a * x + b


def J(a, b, x, y):
    return np.mean((y - (a * x + b)) ** 2)


def J_ableitung_a(a, b, x, y):
    return np.mean(-2 * x * (-a * x - b + y))

def J_ableitung_b(a, b, x, y):
    return np.mean(((-2) * (((-a) * x) - b + y)))


lr = 0.000000000005
a = 1
b = 1
for i in range(0, 500):
    da = J_ableitung_a(a, b, points[:, 0], points[:, 1])
    db = J_ableitung_b(a, b, points[:, 0], points[:, 1])
    a = a - lr * da
    b = b - lr * db * 1e10

    cost = J(a, b, points[:, 0], points[:, 1])
    print("Kosten wenn a = " + str(a) + ": " + str(cost))

xs = np.arange(0, 120000, 10000)
ys = f(a, b, xs)
plt.plot(xs, ys)

plt.scatter(points[:, 0], points[:, 1])
plt.show()