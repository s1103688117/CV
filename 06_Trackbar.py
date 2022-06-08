import cv2
import numpy as np

def callback():
    pass

#创建窗口
cv2.namedWindow('trackbar', cv2.WINDOW_NORMAL)

#创建trackbar
cv2.createTrackbar('R', 'trackbar',0,255,callback)
cv2.createTrackbar('G', 'trackbar',0,255,callback)
cv2.createTrackbar('B', 'trackbar',0,255,callback)
#创建一个背景图片
img = np.zeros((480,640,3),np.uint8)

while True:
    #获取当前trackbar的值
    r = cv2.getTrackbarPos('R','trackbar')
    g = cv2.getTrackbarPos('G', 'trackbar')
    b = cv2.getTrackbarPos('B', 'trackbar')
    #改变图片背景颜色
    img[:]= [b,g,r]
    cv2.imshow('Trackbar',img)

    key = cv2.waitKey(1)
    if key & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
