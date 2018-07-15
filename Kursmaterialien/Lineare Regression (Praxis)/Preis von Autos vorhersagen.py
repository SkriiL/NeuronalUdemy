import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Praxisbeispiel: Preis von Autos bestimmen!
#   -> Partielle Ableitung
#   -> Bias

df = pd.read_csv("./autos_prepared.csv")

points = df[["kilometer", "price"]].values
print(points)

def f(a, x):
    return a * x


def J(a, x, y):
    return np.mean((y - a * x) ** 2)


def J_ableitung_a(a, x, y):
    return np.mean(-2 * x * (y - a * x))


lr = 0.000000000005
a = 1
for i in range(0, 50):
    da = J_ableitung_a(a, points[:, 0], points[:, 1])
    a = a - lr * da

    cost = J(a, points[:, 0], points[:, 1])
    print("Kosten wenn a = " + str(a) + ": " + str(cost))

xs = np.arange(0, 120000, 10000)
ys = f(a, xs)
plt.plot(xs, ys)

plt.scatter(points[:, 0], points[:, 1])
plt.show()