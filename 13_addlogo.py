# 1 引入一张图片
# 2 要有一个LOGO，需要自己创建
# 3 计算图片在什么地方添加，再添加的地方变成黑色
# 4 利用add将logo与图片叠加到一起

import cv2
import numpy as np
#导入图片
img = cv2.imread(r'E:\lenna.png')

#创建LOGO和mask
logo = np.zeros((100,100,3),np.uint8)
mask = np.zeros((100,100),np.uint8)
#绘制logo
logo[20:40, 20:40] = [0,0,255]
logo[30:50, 30:50] = [0,255,0]

mask[20:40, 20:40] = 255
mask[30:50, 30:50] = 255
#对mask按位取反
m = cv2.bitwise_not(mask)
#选择位置添加logo
roi = img[0:100,0:100]
#与m进行与操作
tmp = cv2.bitwise_and(roi,roi,mask=m)
dst = cv2.add(tmp,logo)

img[0:100,0:100] = dst
cv2.imshow('img',img)
# cv2.imshow('tmp',tmp)
# cv2.imshow('m',m)
# cv2.imshow('mask',mask)
# cv2.imshow('logo',logo)
cv2.waitKey(0)
cv2.destroyAllWindows()
