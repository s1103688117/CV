import cv2
import numpy as np

#全局二值化
img = cv2.imread(r'E:\lenna.png')
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret, dst =cv2.threshold(img_gray,180,255,cv2.THRESH_BINARY)
print(dst.shape)

cv2.imshow("img",img)
cv2.imshow("img_gray",img_gray)
cv2.imshow("dst",dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
