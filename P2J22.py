import cv2
import numpy as np

def black_hole(number):
    images = []
    for i in range(1,6):

        img = cv2.imread(f'black hole/{number}/{i}.jpg')
        img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        images.append(img)

    img_result = np.zeros(images[0].shape, dtype='uint8')

    for i in images:
        img_result += (i // len(images))
    cv2.imwrite(f'img_result{number}.jpg', img_result)
black_hole(1)
black_hole(2)
black_hole(3)
black_hole(4)

img_1 = cv2.imread('img_result1.jpg')
img_2 = cv2.imread('img_result2.jpg')
img_3 = cv2.imread('img_result3.jpg')
img_4 = cv2.imread('img_result4.jpg')

img_1_h = cv2.hconcat([img_1, img_2])
img_2_h = cv2.hconcat([img_3, img_4])
img_final = cv2.vconcat([img_1_h,img_2_h])

cv2.imwrite('Practice 2.jpg', img_final)
cv2.imshow('Practice 2', img_final)
cv2.waitKey()

