
import cv2
cv2.namedWindow("colorful_img", cv2.WINDOW_NORMAL)
cv2.setWindowProperty("colorful_img", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

image2 = cv2.imread("photos\\istockphoto-478656454-612x612.jpg")

cv2.imshow("colorful_img", image2)
cv2.waitKey(0)
cv2.destroyAllWindows()
