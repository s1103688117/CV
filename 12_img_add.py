import cv2
import numpy as np

img1 = cv2.imread(r'E:\lenna.png')
print(img1.shape)
img2 = np.ones((512,512,3),np.uint8) * 50
cv2.imshow("origin",img1)

result = cv2.add(img1, img2)
cv2.imshow("result",result)
cv2.waitKey(0)
cv2.destroyAllWindows()