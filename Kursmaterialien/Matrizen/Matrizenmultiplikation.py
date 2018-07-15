import numpy as np

a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

b = np.array([
    [10, 20],
    [30, 40],
    [50, 60]
])

print(a @ b)
print(np.dot(a, b))

c = np.array([
    [1, 2],
    [3, 4]
])
d = np.array([
    [1, 2],
    [3, 4]
])

print(c * d)
print(c @ d)
