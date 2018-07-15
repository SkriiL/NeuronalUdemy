import numpy as np
from operator import xor

a = True
b = True

# (not A) and (not B)
print((not a) and (not b))

# A and B
print(a and b)

# A or B
print(a or b)

# A xor B
print(xor(a, b))