import cv2

image1 = cv2.imread("photos\\istockphoto-108348088-612x612.jpg", cv2.IMREAD_GRAYSCALE)
image2 = cv2.imread("photos\\istockphoto-478656454-612x612.jpg")

cv2.imshow("grey_frog_1", image1)
cv2.imshow("grey_frog_2", image2)

cv2.waitKey(0)
