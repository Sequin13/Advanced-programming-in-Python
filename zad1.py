import cv2
import numpy as np

image = cv2.imread('dir_pics/hum.jpg')
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
mask = np.ones(image.shape[:2], dtype="uint8") * 255

for (x, y, w, h) in faces:
    centerX, centerY = x + w // 2, y + h // 2
    radius = min(w, h) // 2

    cv2.circle(mask, (centerX, centerY), radius, 0, -1)

masked_without_face = cv2.bitwise_and(image, image, mask=mask)

face_mask = np.zeros(image.shape[:2], dtype="uint8")
for (x, y, w, h) in faces:
    centerX, centerY = x + w // 2, y + h // 2
    radius = min(w, h) // 2
    cv2.circle(face_mask, (centerX, centerY), radius, 255, -1)

masked_face_only = cv2.bitwise_and(image, image, mask=face_mask)

# g. Wyświetlanie wyników
cv2.imshow("Origimnal", image)
cv2.imshow("Without face", masked_without_face)
cv2.imshow("Just face", masked_face_only)
cv2.waitKey(0)
cv2.destroyAllWindows()
