import cv2
import numpy as np
###专利问题用不了
img = cv2.imread(r'D:\BaiduNetdiskDownload\1\chess.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

sift = cv2.xfeatures2d.SIFT_create()
kp = sift.detect(gray, NONE)

cv2.drawKeypoints(gray, kp, img)
cv2.imshow('img', img)
cv2.waitKey(0)