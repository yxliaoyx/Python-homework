import numpy as np

a = np.array([54, 27, 66, 77, 10, 0, 72, 74, 59])
b = np.array([52, 90, 94, 85, 53, 59, 35, 59, 86])

c = a.reshape(3, 3)

print(np.may_share_memory(a, c))
# True if a and c share memory

z = np.vstack([a, b]).T
print(z)

z = np.vstack([a, b])
print(z)

print((b > a).sum())

w = b[b > a]
print(w)

boolean_mask = ((b > np.roll(b, 1)) & (b > np.roll(b, -1)))
boolean_mask[[0, -1]] = False
w = b[boolean_mask]
print(w)
