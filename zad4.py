import cv2

image = cv2.imread("photos\\istockphoto-108348088-612x612.jpg", cv2.IMREAD_GRAYSCALE)

cv2.imwrite("saved_photos\\grey_frog.jpg", image)



