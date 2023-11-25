import cv2 as cv 
import numpy as np
import os 
import time
haar_cascade = cv.CascadeClassifier('E:\OpenCv\Face_detection\har_cascade_face.xml')
Dir = r'E:\OpenCv\Face_detection\sample'
feature = []
label = []

def create_train():
    for img in os.listdir(Dir):
        img_path = os.path.join(Dir, img)
        
        img_arrey  = cv.imread(img_path)
        # print(img_arrey)
        # cv.imshow('Person', img_arrey)
        
        gray = cv.cvtColor(img_arrey, cv.COLOR_BGR2GRAY)
        
        face_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=8)
        print(face_rect)
        
        for x,y,w,h in face_rect:
            face_roi = gray[y:y+h, x:x+w]
            feature.append(face_roi)
            label.append(0)
            cv.rectangle(gray, (x,y), (x+w, y+h), (0,255,0), thickness=2)
        # print("i am running ")
            
        # cv.imshow('Person', gray)
        # cv.waitKey(1000)
        # time.sleep(10)

create_train()
print("training done -------------------------")
print(f'Length of the features list: {len(feature)}')

#face recognizer trainig 
features = np.array(feature, dtype='object')
labels = np.array(label, dtype=np.int32)
face_recog = cv.face.LBPHFaceRecognizer_create()

face_recog.train(features, labels)

face_recog.save('face_trained.yml')
np.save('features.npy', features)
np.save('labels.npy', labels)
