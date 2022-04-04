import matplotlib.pyplot as plt
import numpy as np
import skimage.io
img = skimage.io.imread('tiger.png', as_gray=True)
plt.figure(1)
plt.imshow(img, cmap='gray', vmin=0, vmax=255)

rows, cols = img.shape

img_new = img.copy()

half = cols/2

for i in range(rows):
    for j in range(cols):
        if j == half:
            img_new[i][j] = img[i][j]
        else:
            if j < half:
                udaljenost = half - j
                novi_j = int(j+udaljenost*2)
                img_new[i][j] = img[i][novi_j-1]
            else:
                udaljenost = j - half
                novi_j = int(j-udaljenost*2)
                img_new[i][j] = img[i][novi_j-1]


plt.figure(2)
plt.imshow(img_new, cmap='gray', vmin=0, vmax=255)
plt.show()
