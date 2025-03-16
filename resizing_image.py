import cv2
import imutils
import numpy as np


def resize_image(image, scale=None, width=None, height=None, interpolation=cv2.INTER_LINEAR):
    if scale:
        new_width = int(image.shape[1] * scale)
        new_height = int(image.shape[0] * scale)
    elif width and height:
        new_width, new_height = width, height
    elif width:
        ratio = width / float(image.shape[1])
        new_width, new_height = width, int(image.shape[0] * ratio)
    elif height:
        ratio = height / float(image.shape[0])
        new_width, new_height = int(image.shape[1] * ratio), height
    else:
        return image

    return cv2.resize(image, (new_width, new_height), interpolation=interpolation)


image_path = "cat_boom.jpg"
image = cv2.imread(image_path)


def zad_1():
    half_size = resize_image(image, scale=0.5)
    cv2.imshow("50% of the size", half_size)


def zad_2():
    double_size = resize_image(image, scale=2, interpolation=cv2.INTER_LINEAR)
    cv2.imshow("2x of the size", double_size)


def zad_3():
    fixed_size = resize_image(image, width=200, height=300)
    cv2.imshow("200x300", fixed_size)


def zad_4():
    methods = [cv2.INTER_NEAREST, cv2.INTER_LINEAR, cv2.INTER_CUBIC, cv2.INTER_LANCZOS4]
    method_names = ["INTER_NEAREST", "INTER_LINEAR", "INTER_CUBIC", "INTER_LANCZOS4"]
    for i, method in enumerate(methods):
        resized = resize_image(image, scale=3, interpolation=method)
        cv2.imshow(f"Zoom out 3x {method_names[i]}", resized)


def zad_5():
    width_500 = imutils.resize(image, width=500)
    cv2.imshow("Width 500px", width_500)


def zad_6():
    height_400 = imutils.resize(image, height=400)
    cv2.imshow("Height 400px", height_400)


def zad_7():
    down_5x = resize_image(image, scale=0.2, interpolation=cv2.INTER_AREA)
    cv2.imshow("5x less the size with INTER_AREA", down_5x)


def zad_8():
    up_4x_cubic = resize_image(image, scale=4, interpolation=cv2.INTER_CUBIC)
    up_4x_lanczos = resize_image(image, scale=4, interpolation=cv2.INTER_LANCZOS4)
    cv2.imshow("4x more the size with INTER_CUBIC", up_4x_cubic)
    cv2.imshow("4x more the size with INTER_LANCZOS4", up_4x_lanczos)


def zad_9():
    for scale in range(100, 301, 20):
        resized = resize_image(image, scale=scale / 100)
        cv2.imshow(f"Scaling {int(scale)}%", resized)
        cv2.waitKey(500)


def zad_10():
    width_800 = resize_image(image, width=800)
    cv2.imwrite("output_800px.jpg", width_800)
    cv2.imshow("Saved image with 800px", width_800)


if __name__ == "__main__":
    zad_9()
    cv2.waitKey(0)
    cv2.destroyAllWindows()
