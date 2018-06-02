import cv2

img=cv2.imread("/home/avani/Desktop/dogs.jpg")
img2=cv2.imread('/home/avani/Desktop/dog.jpeg')
# r = 100.0 / img.shape[1]
# dim = (100, int(img.shape[0] * r))

# perform the actual resizing of the image and show it
resized = cv2.resize(img2, (100,200),interpolation=cv2.INTER_LINEAR)
print(resized.shape)
img[100:300,300:400]=resized
cv2.imshow("cutpaste",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
