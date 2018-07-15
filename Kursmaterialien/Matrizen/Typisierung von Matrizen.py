import numpy as np

a = np.array([1.5, 2.5, 5])
print(a.dtype)

b = np.array([1, 2, 3], dtype=np.uint8)
b = b.astype(np.float32)
print(b.dtype)

# 2^8 = 256
b[2] = 255
b[2] = b[2] + 5
print(b)