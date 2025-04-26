# import the necessary packages
import numpy as np
import cv2

triangle = np.zeros((300, 300), dtype="uint8")

points = np.array([[150, 25], [50, 275], [250, 275]])

cv2.fillPoly(triangle, [points], 255)
cv2.imshow("Triangle", triangle)

circle = np.zeros((300, 300), dtype="uint8")
cv2.circle(circle, (150, 150), 150, 255, -1)
cv2.imshow("Circle", circle)

bitwiseAnd = cv2.bitwise_and(triangle, circle)
cv2.imshow("AND", bitwiseAnd)
cv2.waitKey(0)

bitwiseOr = cv2.bitwise_or(triangle, circle)
cv2.imshow("OR", bitwiseOr)
cv2.waitKey(0)

bitwiseXor = cv2.bitwise_xor(triangle, circle)
cv2.imshow("XOR", bitwiseXor)
cv2.waitKey(0)

bitwiseNot = cv2.bitwise_not(triangle)
cv2.imshow("NOT Triangle", bitwiseNot)
cv2.waitKey(0)

points_shifted = np.array([[150+50, 25+30], [50+50, 275+30], [250+50, 275+30]])

triangle_shifted = np.zeros((300, 300), dtype="uint8")
cv2.fillPoly(triangle_shifted, [points_shifted], 255)
cv2.imshow("Shifted Triangle", triangle_shifted)

bitwiseAnd_shifted = cv2.bitwise_and(triangle_shifted, circle)
cv2.imshow("AND with Shifted Triangle", bitwiseAnd_shifted)
cv2.waitKey(0)

bitwiseOr_shifted = cv2.bitwise_or(triangle_shifted, circle)
cv2.imshow("OR with Shifted Triangle", bitwiseOr_shifted)
cv2.waitKey(0)

bitwiseXor_shifted = cv2.bitwise_xor(triangle_shifted, circle)
cv2.imshow("XOR with Shifted Triangle", bitwiseXor_shifted)
cv2.waitKey(0)

cv2.destroyAllWindows()
