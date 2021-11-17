import cv2
import numpy as np

images = []
for i in range(0,15):
    img = cv2.imread(f'highway/h{i}.jpg', 0)
    images.append(img)

image_result = np.zeros(images[0].shape, dtype='uint8')

for i in images:
    image_result += i // len(images)

cv2.imwrite('Practice 4.jpg', image_result)
cv2.imshow('Practice 4', image_result)
cv2.waitKey()