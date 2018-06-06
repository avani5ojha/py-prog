import cv2
import numpy as np

cam=cv2.VideoCapture(0)
while cam.isOpened():
    status,frame=cam.read()
    only_red=cv2.inRange(frame,(0,0,40),(30,40,255))
    if np.all(only_red==0):
        print("nothing")
    else:
      cv2.imshow("red",only_red)
      if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cv2.destroyAllWindows()
cam.release()
