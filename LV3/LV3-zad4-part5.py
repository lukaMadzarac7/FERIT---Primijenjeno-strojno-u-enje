import matplotlib.pyplot as plt
import numpy as np
import skimage.io
img = skimage.io.imread('tiger.png', as_gray=True)
plt.figure(1)
plt.imshow(img, cmap='gray', vmin=0, vmax=255)

rows, cols = img.shape

img_new = np.zeros((rows, cols))

divided = cols/4
DrCet_p = divided
DrCet_k = divided*2

for i in range(rows):
    for j in range(cols):
        if j > DrCet_p and j < DrCet_k:
            img_new[i][j] = img[i][j]

plt.figure(2)
plt.imshow(img_new, cmap='gray', vmin=0, vmax=255)
plt.show()
