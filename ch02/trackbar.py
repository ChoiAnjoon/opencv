import numpy as np
import cv2


def on_level_change(pos):
    global img

    value = pos * 16

    # value = np.clip(value, 0, 255)
    # value의 값을 무조껀 0 ~ 255 값으로 셋팅 하는 넘파이 함수를 사용해도 됌
    if value >= 255:
        value = 255

    img[:, :] = value
    cv2.imshow('image', img)


img = np.zeros((480, 640), np.uint8)
cv2.namedWindow('image')
cv2.createTrackbar('level', 'image', 0, 16, on_level_change)

cv2.imshow('image', img)
cv2.waitKey()
cv2.destroyAllWindows()
