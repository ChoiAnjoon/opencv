import sys 
import cv2 

print('Hello, OpenCV', cv2.__version__)

img = cv2.imread('C:\dev\opencv\ch01\cat.bmp')

if img is None:
    print('이미지 없음')
    sys.exit()

cv2.namedWindow('image')
cv2.imshow('image', img)
cv2.waitKey()

cv2.destroyAllWindows()
