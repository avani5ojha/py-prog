import cv2

cam=cv2.VideoCapture(0)

while cam.isOpened():
    x,y=cam.read()
    hsv=cv2.cvtColor(y,cv2.COLOR_BGR2HSV)

    mask=cv2.inRange(hsv,(110,50,50),(130,255,255))

    result=cv2.bitwise_and(y,y,mask=mask)
    cv2.imshow('frame',y)
    cv2.imshow('mask',mask)
    cv2.imshow("cam1",result)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cv2.destroyAllWindows()
cam.release()
