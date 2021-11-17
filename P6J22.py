import cv2

img = cv2.imread('Naser.jpg', 0)

inverted = 255 - img
blurred = cv2.GaussianBlur(inverted, (35,35), 0)
inverted_blurred = 255 - blurred

sketch = img / inverted_blurred
sketch = sketch * 255

cv2.imwrite('Practice 6.jpg', sketch)
cv2.imshow('Practice 6', sketch)
cv2.waitKey()