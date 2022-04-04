import matplotlib.pyplot as plt
import numpy as np
import skimage.io
img = skimage.io.imread('tiger.png', as_gray=True)
plt.figure(1)
plt.imshow(img, cmap='gray', vmin=0, vmax=255)
img_new = img.copy()

img_new = img.copy()
rows, cols = img.shape

for i in range(rows):
    for j in range(cols):
        img_new[i][j] += 45
        if img_new[i][j] > 255:
            alat = img_new[i][j] - 255
            img_new[i][j] -= alat
plt.figure(2)
plt.imshow(img_new, cmap='gray', vmin=0, vmax=255)
plt.show()





