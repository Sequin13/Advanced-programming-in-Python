import cv2
import numpy as np

image = cv2.imread('dir_pics/r8.jpeg')

hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower_red1 = np.array([0, 120, 70])
upper_red1 = np.array([10, 255, 255])
lower_red2 = np.array([170, 120, 70])
upper_red2 = np.array([180, 255, 255])

mask1 = cv2.inRange(hsv_image, lower_red1, upper_red1)
mask2 = cv2.inRange(hsv_image, lower_red2, upper_red2)
mask = mask1 | mask2

result = cv2.bitwise_and(image, image, mask=mask)

cv2.imshow('Original Image', image)
cv2.imshow('Masked Image', result)

cv2.waitKey(0)
cv2.destroyAllWindows()
