import sys
import numpy as np
import cv2


src = cv2.imread('tekapo.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()

cp = (src.shape[1] / 2, src.shape[0] / 2) # (w, h)
rot = cv2.getRotationMatrix2D(cp, 20, 0.5) # cp 기준으로 20도 rotation 후 0.5정도로 영상을 scaling 조정

dst = cv2.warpAffine(src, rot, (0, 0)) # (0, 0) 출력영상의 크기 와 똑같게 출력

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()
