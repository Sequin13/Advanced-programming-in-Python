import cv2
import numpy as np

image1 = cv2.imread('pic_dir\picrs13.jpg', cv2.IMREAD_GRAYSCALE)
image2 = cv2.imread('pic_dir\picrs13_changed.jpg', cv2.IMREAD_GRAYSCALE)

cv2.imshow("Obraz 1", image1)
cv2.imshow("Obraz 2", image2)
cv2.waitKey(0)


difference = cv2.bitwise_xor(image1, image2)

cv2.imshow("Diffrences (XOR)", difference)
cv2.waitKey(0)
cv2.destroyAllWindows()

_, image1_thresh = cv2.threshold(image1, 128, 255, cv2.THRESH_BINARY)
_, image2_thresh = cv2.threshold(image2, 128, 255, cv2.THRESH_BINARY)

difference = cv2.bitwise_xor(image1_thresh, image2_thresh)
