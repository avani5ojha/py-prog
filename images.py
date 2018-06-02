import cv2


#import numpy as np

#img=np.zeros((512,512))
img=cv2.imread('/home/avani/Desktop/dogs.jpg')

#cutimg=img[0:200,0:300]

cv2.line(img,(0,0),(20,30),(0,0,255),3)
cv2.circle(img,(50,50),24,(0,255,0),2)
cv2.putText(img,"heya",(50,60),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),4)
cv2.imshow("cute dog",img)
#cv2.imshow("cut",cutimg)
cv2.waitKey(0)
cv2.destroyAllWindows()
