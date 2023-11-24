    # pip install opencv-python==4.5.2
import cv2
# from controller import doorAutomate
import time
from database import *

def back_camera():

    video=cv2.VideoCapture(1)


    facedetect = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read("Trainer.yml")

    # imgBackground = cv2.imread("background.png")
    personid=[]

# def print_data(serial):
#     if(serial != 'None'):
#         get_data_by_face(serial)  
    while True:

        serial=None
        conf=0
        ret,frame=video.read()
        gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = facedetect.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
            serial, conf = recognizer.predict(gray[y:y+h, x:x+w])
            # print(conf)
            # print(serial)
            if conf<50:
                cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), 1)
                cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
                cv2.rectangle(frame,(x,y-40),(x+w,y),(0,0,255),-1)
            # cv2.putText(frame, (x, y-10),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,255),2)
            else:
                cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), 1)
                cv2.rectangle(frame,(x,y),(x+w,y+h),(50,50,255),2)
                cv2.rectangle(frame,(x,y-40),(x+w,y),(50,50,255),-1)
            # cv2.putText(frame, (x, y-10),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,255),2)
    
        frame=cv2.resize(frame, (640, 480))
        # imgBackground[162:162 + 480, 55:55 + 640] = frame
        cv2.imshow("Frame",frame)
        # print("hi1")
        if (serial not in personid) :
        # personid.append(serial)
            # print("hi2")
            if conf < 80:
                # print("hi3")
                personid.append(serial)
        # get_data_by_face(serial)
        # print_data(serial)
                if serial!=None:
                    print("hi4")
                    leaving_timeentry(serial)
        k=cv2.waitKey(1)
    
        if k==ord('o') and conf>50:
        # doorAutomate(0)
            time.sleep(10)
        # doorAutomate(1)
        if k==ord("q"):
            break

    # print(personid)
# leaving_timeentry(serial)
# get_data_by_face(serial)
    video.release()
    cv2.destroyAllWindows()

# back_camera()