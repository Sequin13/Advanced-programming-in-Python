import cv2
import matplotlib.pyplot as plt

image = cv2.imread('kostka.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
resized = cv2.resize(image, (300, int(300 * image.shape[0] / image.shape[1])))
resized_gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

_, thresh = cv2.threshold(resized_gray, 140, 255, cv2.THRESH_BINARY)

modes = {
    "RETR_EXTERNAL": cv2.RETR_EXTERNAL, # najmniej wrażliwy na niedokładności
    "RETR_LIST": cv2.RETR_LIST, # wysoka wrażliwość na niedokładność
    "RETR_TREE": cv2.RETR_TREE # nie jestem w stanie znaleźć różnicy wizualnej między RETR_LIST a RETR_TREE
}

plt.figure(figsize=(15, 5))

for i, (mode_name, mode) in enumerate(modes.items()):
    contours, _ = cv2.findContours(thresh, mode, cv2.CHAIN_APPROX_SIMPLE)

    drawn = resized.copy()
    cv2.drawContours(drawn, contours, -1, (0, 0, 255), 2)

    plt.subplot(1, 3, i+1)
    plt.imshow(cv2.cvtColor(drawn, cv2.COLOR_BGR2RGB))
    plt.title(mode_name)
    plt.axis('off')

plt.tight_layout()
plt.show()
