import cv2
import matplotlib.pyplot as plt

image = cv2.imread('kostka.jpg', cv2.IMREAD_GRAYSCALE)

height, width = image.shape
new_width = 300
scale = new_width / width
new_height = int(height * scale)
resized_image = cv2.resize(image, (new_width, new_height))

thresholds = [100, 140, 180]
results = []

for t in thresholds:
    _, thresh_img = cv2.threshold(resized_image, t, 255, cv2.THRESH_BINARY)
    results.append((t, thresh_img))

plt.figure(figsize=(12, 4))
for i, (t, img) in enumerate(results):
    plt.subplot(1, 3, i+1)
    plt.imshow(img, cmap='gray')
    plt.title(f'Prog: {t}')
    plt.axis('off')
plt.tight_layout()
plt.show()
