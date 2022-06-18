import cv2
import numpy as np

maxCorners = 1000
ql = 0.01
minDistance =10

img = cv2.imread(r'D:\BaiduNetdiskDownload\1\chess.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Shi-Tomasi角点检测
corners = cv2.goodFeaturesToTrack(gray, maxCorners, ql, minDistance)
corners = np.int0(corners)

for i in corners:
    x, y = i.ravel()
    cv2.circle(img, (x, y), 3, (255, 0, 0), -1)

cv2.imshow('Tomasi', img)
cv2.waitKey(0)
