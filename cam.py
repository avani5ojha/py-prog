import cv2

cam=cv2.VideoCapture(0)
while cam.isOpened():
    print("wrking")
    status,frame=cam.read()
    new=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("cam0",frame)
    cv2.imshow("cam1",new)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cv2.destroyAllWindows()
cam.release()
