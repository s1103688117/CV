import cv2

cv2.namedWindow('new',cv2.WINDOW_AUTOSIZE)
cv2.resizeWindow('new',1920,1080)
cv2.imshow('new',0)
cv2.waitKey(0)
# key = cv2.waitKey()
# if key == 'q':

cv2.destroyAllWindows()