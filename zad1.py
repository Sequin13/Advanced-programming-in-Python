import cv2
image = cv2.imread("photos\\istockphoto-478656454-612x612.jpg")
if image is None:
    print("Error: can't read image")
    exit()
else:
    print("Image has been read succesfuly")
    