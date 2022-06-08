import cv2
cv2.namedWindow('img',cv2.WINDOW_AUTOSIZE)
img = cv2.imread('E:\B.png')
cv2.imshow('img',img)
key = cv2.waitKey(0)
if key & 0xFF == ord('q'):
    exit()

cv2.destroyAllWindows()