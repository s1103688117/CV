# 基本功能
# 可以通过鼠标进行基本图形的绘制
# 1 可以画线，当用户按下l键，即选择画线，此时，滑动鼠标即可画线
# 2 可以画矩形，当用户按下r键，即选择画矩形，此时，滑动鼠标即可画矩形
# 3 可以画圆，当用户按下c键，即选择画圆，此时，滑动鼠标即可画圆
# ....
import cv2
import numpy as np
# cur_shape 0-draeline, 1-drawrectangle, 2-drawcircle
startpos = (0,0)
cur_shape = 0
#鼠标回调函数
def mouse_callback(event, x, y, flages, userdata):
    # print(event, x, y, flages, userdata)
    global startpos, cur_shape
    if (event & cv2.EVENT_LBUTTONDOWN == cv2.EVENT_LBUTTONDOWN):
        startpos = (x, y)
    elif (event & cv2.EVENT_LBUTTONUP == cv2.EVENT_LBUTTONUP):
        if cur_shape == 0:
            cv2.line(img, startpos, (x,y), (0, 0, 255))
        elif cur_shape == 1:
            
            cv2.rectangle(img,startpos, (x, y), (0, 0, 255))
        elif cur_shape == 2:
            a = (x - startpos[0])
            b = (y - startpos[1])
            r = int((a**2+b**2)**0.5)
            cv2.circle(img, startpos,r,(0, 0, 255))
        else:
            print('error:no shape')



#创建窗口
cv2.namedWindow('drawshape',cv2.WINDOW_NORMAL)

#设置鼠标回调
cv2.setMouseCallback('drawshape',mouse_callback, '123')
#显示窗口和背景
img = np.zeros((480, 640, 3),np.uint8)

while True:
    cv2.imshow('drawshape',img)
    key = cv2.waitKey(1)
    if key & 0xFF == ord('q'):
        break
    if key & 0xFF == ord('l'): #drawline
        cur_shape = 0
    if key & 0xFF == ord('r'): #drawrectangle
        cur_shape = 1
    if key & 0xFF == ord('c'): #drawcircle
        cur_shape = 2