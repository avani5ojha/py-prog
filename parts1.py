import cv2
import numpy

row=int(raw_input("enter row"))
col=int(raw_input("enter col"))

img=cv2.imread("/home/avani/Desktop/dogs.jpg")
img2=cv2.imread("/home/avani/Desktop/dogs.jpg")

r=384
c=768
flag=0
resize=cv2.resize(img2,(col,row))


if r%row==0 and c%col!=0:
  for i in range(0,c-col,(col)):
    for j in range(0,r,(row)):
    #cv2.rectangle(img,(0,0),(row,col),2)

       img[j:row+j,i:col+i]=resize
       flag=flag+1

       cv2.imshow("bl",img)
       cv2.waitKey(0)
       cv2.destroyAllWindows()

if c%col==0 and r%row!=0:
  for i in range(0,c,(col)):
    for j in range(0,r-row,(row)):
    #cv2.rectangle(img,(0,0),(row,col),2)

       img[j:row+j,i:col+i]=resize
       flag=flag+1

       cv2.imshow("bl",img)
       cv2.waitKey(0)
       cv2.destroyAllWindows()

if r%row==0 and c%col==0:
  for i in range(0,c,(col)):
    for j in range(0,r,(row)):
    #cv2.rectangle(img,(0,0),(row,col),2)

       img[j:row+j,i:col+i]=resize
       flag=flag+1

       cv2.imshow("bl",img)
       cv2.waitKey(0)
       cv2.destroyAllWindows()

if r%row!=0 and c%col!=0:
  for i in range(0,c-col,(col)):
    for j in range(0,r-row,(row)):
    #cv2.rectangle(img,(0,0),(row,col),2)

       img[j:row+j,i:col+i]=resize
       flag=flag+1

       cv2.imshow("bl",img)
       cv2.waitKey(0)
       cv2.destroyAllWindows()

print("total no. of rectangles:",flag)

# for i in range(0,c,col):
#     #cv2.rectangle(img,(0,0),(row,col),2)
#     black[0:row,i:col+i]=img[0:row,i:col+i]
#     cv2.imshow("bl",black)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
