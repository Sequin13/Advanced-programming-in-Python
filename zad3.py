import cv2

image = cv2.imread("photos\\images_nature.jpg", cv2.IMREAD_GRAYSCALE)
grey_photo_values = image.shape
print(grey_photo_values)
# no third value - there is only 1 channel in grey images




