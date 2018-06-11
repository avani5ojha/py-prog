import cv2

img=cv2.imread("/home/avani/Desktop/dogs.jpg")

#print(img.shape)

#print(cv2.split(img))

b=[20,30,40]

for i in range(384):
    for j in range(768):
        a=img[i][j][:3]



        a=a+b

        img[i][j][:3]=a


cv2.imshow("shade",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
