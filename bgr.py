import cv2

img=cv2.imread("/home/avani/Desktop/dogs.jpg")

print(img.shape)

print(cv2.split(img))

print(type(img))

# for i in range(384):
#     for j in range(768):
#         img[i][j]
