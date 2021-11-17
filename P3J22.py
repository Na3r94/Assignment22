import cv2

img_board_origin = cv2.imread('board - origin.bmp', 0)
img_board_test = cv2.imread('board - test.bmp', 0)

img_board_test = cv2.flip(img_board_test, 1)

img_final = cv2.subtract(img_board_origin,img_board_test)

cv2.imwrite('Practice 3.jpg', img_final)
cv2.imshow('Practice 3', img_final)
cv2.waitKey()