import cv2
import numpy as np
import imutils


def shift_image(image_path, x, y):
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Can't load image")
        return

    height, width = image.shape[:2]

    M = np.float32([[1, 0, x], [0, 1, y]])

    shifted_image = cv2.warpAffine(image, M, (width, height))

    cv2.imshow('Original image', image)
    cv2.imshow('Shifted image', shifted_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


image_path = 'jpgs\\catameme.jpg'


def zad_1():
    shift_image(image_path, 30, 40)


def zad_2():
    shift_image(image_path, -20, -50)


def zad_3():
    image = cv2.imread(image_path)
    imgx, imgy = image.shape[:2]
    shift_image(image_path, imgx / 2 + 20, imgy / 2 + 20)


def shift_image_with_imutils(image_path, x, y):
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Can't load image")
        return

    shifted_image_imutils = imutils.translate(image, x, y)

    cv2.imshow('Original image', image)
    cv2.imshow('Shifted image - imutils.translate', shifted_image_imutils)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


def zad_4():
    shift_image_with_imutils(image_path, 100, 50)


def zad_5():
    x = input("Insert value of shift image horizontally: ")
    y = input("Insert value of shift image vertically: ")
    shift_image(image_path, x, y)


if __name__ == "__main__":
    zad_5()
