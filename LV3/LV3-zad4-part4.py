import matplotlib.pyplot as plt
import numpy as np
import skimage.io
img = skimage.io.imread('tiger.png', as_gray=True)
plt.figure(1)
plt.imshow(img, cmap='gray', vmin=0, vmax=255)

rows, cols = img.shape

sr = int(rows/10)
sc = int(cols/10)
small = np.zeros((sr, sc))

for i in range(sr):
    for j in range(sc):
        small[i, j] = img[10*i, 10*j]

plt.figure(2)
plt.imshow(small, cmap='gray', vmin=0, vmax=255)
plt.show()
