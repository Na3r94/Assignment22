import cv2

img_me = cv2.imread('Naser.jpg', 0)
img_tom = cv2.imread('Tom.jpg', 0)

img_me = cv2.resize(img_me, (300, 300))
img_tom = cv2.resize(img_tom, (300, 300))

img_1 = img_me // 3 + img_me // 3 + img_tom // 3

img_2 = img_me // 3 + img_tom // 3 + img_tom // 3

image_result = cv2.hconcat([img_me,img_1,img_2,img_tom])

cv2.imwrite('Practice 5.jpg', image_result)
cv2.imshow('Practice 5', image_result)
cv2.waitKey()