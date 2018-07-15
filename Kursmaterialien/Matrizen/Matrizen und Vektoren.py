import numpy as np

a = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8]
])
b = np.array([1, 1, 0, 0])

print(a * b)

a2 = np.array([
    [1, 5],
    [2, 6],
    [3, 7],
    [4, 8]
])
b2 = np.array([1, 1, 0, 0])
print(a2.T * b2)