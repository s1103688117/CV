import  cv2

#创建VideoWriter为写多媒体文件
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
vw = cv2.VideoWriter('E:\out.mp4',fourcc,25,(1280,720))
#创建窗口
cv2.namedWindow('video',cv2.WINDOW_AUTOSIZE)
#获取视频设备
cap = cv2.VideoCapture(0)
#判断摄像头是否打开
while cap.isOpened():
    #从摄像头读取视频帧
    ret,frame = cap.read()
    if ret == True:
        #显示
        cv2.imshow('video',frame)
        #写数据到多媒体文件
        vw.write(frame)
        key = cv2.waitKey(1)


        if key & 0xFF == ord('q'):
            break
    else:
        break

#释放VideoCaputure
cap.release()

#释放VideoWriter
vw.release()

cv2.destroyAllWindows()