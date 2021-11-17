import cv2

img_1 = cv2.imread('a.tif')
img_1 = cv2.cvtColor(img_1, cv2.COLOR_RGB2GRAY)

img_2 = cv2.imread('b.tif')
img_2 = cv2.cvtColor(img_2, cv2.COLOR_RGB2GRAY)

img_result = cv2.subtract(img_2,img_1)
rows, cols = img_result.shape

for i in range(rows):
    for j in range(cols):
        img_result[i, j] = 255 - img_result[i, j]
cv2.imshow('Practice 1', img_result)
cv2.waitKey()