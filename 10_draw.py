import cv2
import numpy as np

img = np.zeros((480,640,3),np.uint8)

#划线
cv2.line(img, (10, 20), (300, 400), (0, 0, 255), 5)
#矩形
cv2.rectangle(img, (10, 10), (100, 100), (0, 0, 255), -1)
#圆
cv2.circle(img, (320, 250), 100, (0, 0, 255), 5)
#椭圆
cv2.ellipse(img, (320, 250), (100, 50), 0, 0, 360, (0, 0, 255), -1)

#画多边形
pts = np.array([(300,10), (150,100), (450,100)])
cv2.polylines(img,[pts],True, (0,0,255))
#填充多边形
cv2.fillPoly(img, [pts], (255,255,0))
#绘制文本
cv2.putText(img,'hello world',(10,400),cv2.FONT_HERSHEY_PLAIN,3,(255,255,0))

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()