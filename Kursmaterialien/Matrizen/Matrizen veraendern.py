import numpy as np

a = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [1, 2, 3],
    [4, 5, 6]
])

# print(a.reshape(6, 1))
# print(a.reshape(6, -1))

print(a.reshape(-1))