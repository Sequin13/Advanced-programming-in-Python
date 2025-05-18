import cv2
import matplotlib.pyplot as plt

image = cv2.imread('kostka.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

scales = [1.0, 0.75, 0.5, 0.25]

plt.figure(figsize=(15, 5))

for i, scale in enumerate(scales):
    resized = cv2.resize(gray, (0, 0), fx=scale, fy=scale)
    color_copy = cv2.cvtColor(resized, cv2.COLOR_GRAY2BGR)

    _, thresh = cv2.threshold(resized, 140, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(color_copy, contours, -1, (0, 0, 255), 2)
    plt.subplot(1, 4, i+1)
    plt.imshow(cv2.cvtColor(color_copy, cv2.COLOR_BGR2RGB))
    plt.title(f'Skala {int(scale * 100)}% - Konturów: {len(contours)}')
    plt.axis('off')

plt.tight_layout()
plt.show()
