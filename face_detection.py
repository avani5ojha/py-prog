import cv2

face_c=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img=cv2.imread("face-9.jpg")

face=face_c.detectMultiScale(img, scaleFactor=1.01, minNeighbors=5)

for x,y,w,h in face:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255))

cv2.imshow("face",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
