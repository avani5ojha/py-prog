import cv2
import numpy

black=numpy.zeros((384,768,3))


img=cv2.imread("/home/avani/Desktop/dogs.jpg",1)

newimg=img[0:192,0:768]


black[0:192,0:768]=img[0:192,0:768]

cv2.imshow("bl",newimg)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imshow("bl",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
