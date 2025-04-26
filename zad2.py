import cv2
import numpy as np

image = cv2.imread('dir_pics/big_eyes.jpg')

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, 5)

for (x, y, w, h) in faces:
    face_region = image[y:y + h, x:x + w]
    face_gray = gray[y:y + h, x:x + w]

    eyes = eye_cascade.detectMultiScale(face_gray)
    mask = np.ones_like(image) * 255
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(mask, (x + ex, y + ey), (x + ex + ew, y + ey + eh), (0, 0, 0), -1)  # Zasłonięcie na czarno

    masked = cv2.bitwise_and(image, mask)

    cv2.imshow("Original", image)
    cv2.imshow("Without eyes", masked)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
