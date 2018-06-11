import cv2
cam=cv2.VideoCapture(0)

width=cam.get(cv2.CAP_PROP_FRAME_WIDTH)
height=cam.get(cv2.CAP_PROP_FRAME_HEIGHT)

video_format=cv2.VideoWriter_fourcc(*'XVID')
video_output=cv2.VideoWriter('first_vid.avi',video_format,30.0,(int(width),int(height)))

face_c=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while cam.isOpened():

  x,frame=cam.read()

  face=face_c.detectMultiScale(frame, scaleFactor=1.05, minNeighbors=5)


  for x,y,w,h in face:
    cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3)

  cv2.imshow("cam",frame)
  if cv2.waitKey(1) & 0xFF==ord('q'):
      break


cv2.waitKey(0)
cv2.destroyAllWindows()
cam.release()
