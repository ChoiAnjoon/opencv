import sys
import numpy as np
import cv2


img = cv2.imread('cat.bmp', cv2.IMREAD_GRAYSCALE)

if img is None:
    print('Image load failed!')
    sys.exit()

cv2.namedWindow('image')
cv2.imshow('image', img)

while True:
    # 키코드를 한변수에 담아 놓기 
    keycode = cv2.waitKey()
    # i, I 키를 누르면 영상을 반전해서 보여줌
    if keycode == ord('i') or keycode == ord('I'):
        img = ~img
        cv2.imshow('image', img)
    # ESC 키를 누르면 break
    elif keycode == 27:
        break

cv2.destroyAllWindows()
