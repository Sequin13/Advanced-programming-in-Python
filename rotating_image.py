import cv2
import numpy as np
import imutils


def rotate_image(image, angle, center=None, scale=1.0):
    (h, w) = image.shape[:2]
    if center is None:
        center = (w // 2, h // 2)

    M = cv2.getRotationMatrix2D(center, angle, scale)
    rotated = cv2.warpAffine(image, M, (w, h))
    return rotated


def rotate_bound(image, angle):
    return imutils.rotate_bound(image, angle)


def display_images(original, transformed, title="Image after rotate"):
    cv2.imshow("Original", original)
    cv2.imshow(title, transformed)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


image = cv2.imread("maxwell.jpg")


def zad_1():
    rotated_45 = rotate_image(image, 45)
    display_images(image, rotated_45, "45 degree rotate")


def zad_2():
    rotated_neg_90 = rotate_image(image, -90)
    display_images(image, rotated_neg_90, "-90 degree rotate")


def zad_3():
    rotated_corner = rotate_image(image, 30, (0, 0))
    display_images(image, rotated_corner, "Top-left corner 30 degree rotate")


def zad_4():
    angle = float(input("Insert degree of rotate"))
    rotated_custom = rotate_image(image, angle)
    display_images(image, rotated_custom, f"{angle} degree rotate - from user")


def zad_5():
    rotated_180 = imutils.rotate(image, 180)
    display_images(image, rotated_180, "180 degree rotate - using imutils")


def zad_6():
    rotated_bound = rotate_bound(image, -33)
    display_images(image, rotated_bound, "-33 degree rotate - without cutting edges")


def zad_7():
    rotated_warpAffine = rotate_image(image, 60)
    rotated_imutils = imutils.rotate(image, 60)
    display_images(rotated_warpAffine, rotated_imutils, "Compareing warpAffine and imutils.rotate")


def zad_8():
    sequential_rotation = rotate_image(rotate_image(rotate_image(image, 30), 30), 30)
    rotated_90 = rotate_image(image, 90)
    display_images(sequential_rotation, rotated_90, "3 x 30 degree sequence rotate vs 90 degree rotate")


def zad_9():
    rotated_75 = rotate_image(image, 75)
    cv2.imwrite("rotated_output.jpg", rotated_75)
    display_images(image, rotated_75, "Rotate and save")


def zad_10():
    for angle in range(0, 361, 15):
        rotated_loop = rotate_image(image, angle)
        cv2.imshow("Rotate in loop", rotated_loop)
        cv2.waitKey(500)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    zad_10()
    cv2.destroyAllWindows()
