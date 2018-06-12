import os
import numpy as np
from PIL import Image
import cv2

recognizer=cv2.face.LBPHFaceRecognizer_create()
path="/home/avani/project/training_data"

face_c=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")



def getImageWithId(path):
    faces=[]
    ids=[]
    subfolders=os.listdir(path)
    for folders in subfolders:

            folder_path=path+"/"+folders
            # print(folder_path)
            images=os.listdir(folder_path)
            for image_names in images:
                image_path=folder_path+"/"+image_names
                # print(image_path)
                # readimage=cv2.imread(image_path)
                faceImg=Image.open(image_path).convert("L")


                faceNp=np.array(faceImg,'uint8')
                id1=image_path.split('/')[-1]
                id=int(id1.split('-')[0])
                faces.append(faceNp)
                ids.append(id)
                # cv2.imshow("training", faceNp)
                # cv2.waitKey(10)
    return np.array(ids), faces
#getting the name of user
def get_folder_name(path,id):

    subfolders=os.listdir(path)
    for folders in subfolders:

            folder_path=path+"/"+folders
            # print(folder_path)
            images=os.listdir(folder_path)
            for image_names in images:
                image_path=folder_path+"/"+image_names
                # print(image_path)
                # readimage=cv2.imread(image_path)
                faceImg=Image.open(image_path).convert("L")


                faceNp=np.array(faceImg,'uint8')
                id1=image_path.split('/')[-1]
                id2=int(id1.split('-')[0])
                if id2==id:
                    return folders


ids,faces=getImageWithId(path)
recognizer.train(faces,ids)
recognizer.write("/home/avani/project/trained_data.yml")

cam=cv2.VideoCapture(0)

recognizer.read("/home/avani/project/trained_data.yml")
user=0
while cam.isOpened():
    x,frame=cam.read()
    if not frame is None:
        gray_y=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        face=face_c.detectMultiScale(frame, scaleFactor=1.05, minNeighbors=5)
        for x,y,w,h in face:
          cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3)
          user,confidence=recognizer.predict(gray_y[x:x+w,y:y+h])

          user=str(get_folder_name(path,user))

          cv2.putText(frame,str(user),(x,y),cv2.FONT_HERSHEY_SIMPLEX,2,(255,0,0),2,cv2.LINE_AA)
        cv2.imshow("recogizer",frame)
        if cv2.waitKey(1) &  0xFF==ord('q'):
          break


cv2.destroyAllWindows()
cam.release()
