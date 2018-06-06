import cv2,transforms

cam=cv2.VideoCapture(0)

width=cam.get(cv2.CAP_PROP_FRAME_WIDTH)
height=cam.get(cv2.CAP_PROP_FRAME_HEIGHT)

video_format=cv2.VideoWriter_fourcc(*'XVID')
video_output=cv2.VideoWriter('first_vid.avi',video_format,10.0,(int(width),int(height)))

while cam.isOpened():
    x,y=cam.read()
    #only_red=cv2.inRange(y,(0,0,40),(30,40,255))
    red = RGBTransform().mix_with((255, 0, 0),factor=.30).applied_to(y)

    cv2.imshow("cam",y)
    video_output.write(y)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cv2.destroyAllWindows()
cam.release()
