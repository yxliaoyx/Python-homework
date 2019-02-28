import numpy as np
import matplotlib.pyplot as plt

data = np.load('mnist.npz')

X_train = data['X_train']  # shape = (60000, 28, 28)
y_train = data['y_train']  # shape = (60000,)

S = np.ndarray(shape=(100, 28, 28))

for i in range(10):
    S[i * 10:(i + 1) * 10] = X_train[y_train == i][:10]

pixels = S.reshape((-1, 28, 28))

pixels = np.insert(pixels, pixels.shape[1], 255, 1)
pixels = np.insert(pixels, pixels.shape[2], 255, 2)

pixels = pixels.reshape((10, 10, 29, 29)).transpose((0, 2, 1, 3)).reshape((-1, 29, 29))

plt.imshow(pixels.reshape((-1, 290)), cmap='gray')

plt.show()
