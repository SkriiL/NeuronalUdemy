import numpy as np

a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("a.shape: " + str(a.shape))

print("np.sum(a): " + str(np.sum(a)))
print("np.sum(a, axis=0): " + str(np.sum(a, axis=0)))
print("np.sum(a, axis=1): " + str(np.sum(a, axis=1)))

print("np.mean(a): " + str(np.mean(a)))
print("np.mean(a, axis=0): " + str(np.mean(a, axis=0)))
print("np.mean(a, axis=1): " + str(np.mean(a, axis=1)))