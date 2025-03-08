import cv2

image = cv2.imread("photos\\istockphoto-108348088-612x612.jpg")
(h, w, c) = image.shape

print(f'channels: {c}')
