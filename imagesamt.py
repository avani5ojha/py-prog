import cv2

img=cv2.imread("/home/avani/Desktop/dogs.jpg")

# print("how much portion of the image do you want")
# row1=int(input())
# col1=int(input())
# row2=int(input())
# col2=int(input())
#
# newimg=img9[row1:col1,row2:col2]

choice=raw_input("how much portion of the image do to want?")
if choice=="half":
    c1=raw_input("upper or lower,left,right")

    if c1=="upper":
        newimg=img[0:192,0:768]
    if c1=="lower":
        newimg=img[192:384,0:768]
    if c1=="left":
        newimg=img[0:384,0:384]
    if c1=="right":
        newimg=img[0:384,384:768]
if choice=="one third":
      c1=raw_input("upper or lower,left,right")

      if c1=="upper":
          newimg=img[0:126,0:768]
      if c1=="lower":
          newimg=img[252:384,0:768]
      if c1=="mid hori":
           newimg=img[126:252,0:768]
      if c1=="mid verti":
           newimg=img[0:384,256:512]
      if c1=="left":
          newimg=img[0:384,0:256]
      if c1=="right":
          newimg=img[0:384,512:768]

if choice=="one forth":
     c1=raw_input("upper or lower,left,right")

     if c1=="upper":
         newimg=img[0:96,0:768]
     if c1=="lower":
         newimg=img[288:384,0:768]
     if c1=="mid hori 1":
          newimg=img[96:288,0:768]
     if c1=="mid hori 2":
          newimg=img[288:384,0:768]
     if c1=="left":
         newimg=img[0:384,0:192]
     if c1=="mid verti 1":
         newimg=img[0:384,192:384]
     if c1=="mid verti 2":
        newimg=img[0:384,384:588]
     if c1=="right":
        newimg=img[0:384,588:784]





cv2.imshow("cut image",newimg)
cv2.waitKey(0)
cv2.destroyAllWindows()
