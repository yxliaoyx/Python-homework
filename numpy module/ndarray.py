import numpy as np

A = np.zeros(shape=(200, 200), dtype=np.float)
print(A)

A[100] = 100
print(A)

A[:, 1::2] = 500
print(A)

B = A.copy()
print(B)
