import numpy as np
import matplotlib.pyplot as plt

x_train = np.array([
    [0.0, 0.0],
    [0.0, 1.0],
    [1.0, 0.0],
    [1.0, 1.0]
])

y_train = np.array([
    0.0,
    0.0,
    0.0,
    1.0
])


def s(x):
    return 1 / (1 + np.exp(-x))


def f(w, b, xs):
    rs = []
    for x in xs:
        sum = 0
        for i in range(0, len(w)):
            sum += w[i] * x[i]
        r = s(sum + b)
        rs.append(r)
    return np.array(rs)


def j(w, b, x, y):
    return -np.mean(y * np.log(f(w, b, x)) + (1 - y) * np.log(1 - f(w, b, x)))


def j_ableitung_w(w, b, x, y):
    rs = []
    for i in range(0, len(w)):
        rs.append(np.mean(x[:, i] * (f(w, b, x) - y)))
    return np.array(rs)


def j_ableitung_b(w, b, x, y):
    return np.mean(f(w, b, x) - y)


w = np.array([1.0, 1.0])
b = 1
rate = 0.1
for i in range(0, 1000):
    dw = j_ableitung_w(w, b, x_train, y_train)
    db = j_ableitung_b(w, b, x_train, y_train)

    w -= rate * dw
    b -= rate * db
    cost = j(w, b, x_train, y_train)
    print("Kosten: ", cost)

print("w0 = ", w[0])
print("w1 = ", w[1])
print("b = ", b)

print(f(w, b, [[1.0, 1.0], [0.0, 1.0]]))
