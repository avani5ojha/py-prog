import cv2

img1=cv2.imread("/home/avani/Desktop/dogs.jpg")
img2=cv2.imread("/home/avani/Desktop/merge.jpeg")
print(img1.shape)

newimg=cv2.addWeighted(img1,0.8,img2,0.4,0)
cv2.imshow("added",newimg)
cv2.waitKey(0)
cv2.destroyAllWindows()
