import cv2 as cv
import numpy as np
import base64


def base64_to_img(b64):
    decoded_data = base64.b64decode(b64)
    np_data = np.fromstring(decoded_data, np.uint8)
    img = cv.imdecode(np_data, cv.IMREAD_UNCHANGED)
    return img

def img_to_b64(img):
    retval, buffer = cv.imencode(".jpg", img)
    bytes_b64 = base64.b64encode(buffer)
    b64 = bytes_b64.decode("utf-8")
    return b64

def sobel(img):
    return cv.Sobel(img, cv.CV_32F, 1, 0)
    # return cv.Sobel(img, cv.CV_32F, 1, 1)

def get_linear_bound(img):
    non_empty = [i for i, row in enumerate(img) if np.any(row)]
    first, last = non_empty[0], non_empty[-1]
    # what if it has all non empty?
    return first, last

def get_sobel_boundaries(img):
    top, bottom = get_linear_bound(img)
    left, right = get_linear_bound(np.transpose(img)) # gotta fix this
    return (top, right, bottom, left)


def crop_image(img_b64):
    base_b64, img_b64 = img_b64.split(",")

    img = base64_to_img(img_b64)
    # create mask and calculate boundaries
    img_sobel = sobel(img)
    top, right, bottom, left = get_sobel_boundaries(img_sobel)
    # apply and crop image
    cropped_img = img[top:bottom, ] # gotta fix this, its not taking horizontal ones into account

    b64 = img_to_b64(cropped_img)
    # print(b64[0:100])
    cropped_img_b64 = base_b64 + "," + b64

    return cropped_img_b64


if __name__ == "__main__":
    # IMG_BASE64 = get_test_base64()
    # crop_image(IMG_BASE64)
    pass