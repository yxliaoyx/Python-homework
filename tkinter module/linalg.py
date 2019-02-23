import numpy as np

A = np.mat("4 3 2;-2 4 -3;1 -1 1")
b = np.array([9, 8, 7])

print(np.linalg.solve(A, b))
