import cv2
cv2.namedWindow('img',cv2.WINDOW_AUTOSIZE)
img = cv2.imread('E:\B.png')
while True:
    cv2.imshow('img',img)
    key = cv2.waitKey(0)
    if key & 0xFF == ord('q'):
        break
    elif key & 0xFF == ord('s'):
        cv2.imwrite('E:\B_save.png',img)

cv2.destroyAllWindows()