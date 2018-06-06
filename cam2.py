import cv2
import numpy as np

status=[]
frame=[]


cam=cv2.VideoCapture(0)
for i in range(10000):
 if cam.isOpened():
    print("wrking")
    status.append(0)
    frame.append(0)
    status[i],frame[i]=cam.read()
    cv2.imwrite("face-"+str(i)+".jpg",frame[i])
cv2.destroyAllWindows()
cam.release()
