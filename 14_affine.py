import cv2
import numpy as np
#导入图片
img = cv2.imread(r'E:\lenna.png')
#图像平移
M = np.float32([[1,0,100], [0,1,0]])
new = cv2.warpAffine(img, M, (512,512))
cv2.imshow('img',img)
cv2.imshow('new',new)
cv2.waitKey(0)
cv2.destroyAllWindows()