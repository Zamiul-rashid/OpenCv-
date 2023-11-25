import cv2 as cv 
import numpy as np

haar_cascade = cv.CascadeClassifier('E:\OpenCv\Face_detection\har_cascade_face.xml')

# features = np.load(r'E:\OpenCv\Face_detection\features.npy', allow_pickle=True)

# labels = np.load('.\Face_detection\labels.npy')

facer_recog = cv.face.LBPHFaceRecognizer_create()

facer_recog.read(r'E:\OpenCv\Face_detection\face_trained.yml')


img = cv.imread(r"E:\OpenCv\Face_detection\samp2.jpg")

# img = cv.resize(img, (500,500))
grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  

cv.imshow('Person', img)

#detect 

face_rect = haar_cascade.detectMultiScale(grey, scaleFactor=1.1, minNeighbors=1)


for x, y, w, h in face_rect:
    face_roi = grey[y:y+h, x:x+w]
    
    label, confidence = facer_recog.predict(face_roi)
    
    # Ensure confidence is within 0-100% range
    normalized_confidence = (100 - confidence)  # Reverse confidence for LBPH recognizer
    
    print(f'A confidence of {normalized_confidence:.2f}% for label {label}')
    
    cv.putText(img, f'Confidence: {normalized_confidence:.2f}%', (x, y - 10),
               cv.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)

cv.imshow('Detected Face', img)
cv.waitKey(0)

    
# cv.imshow('Detected Face', img)
    
cv.waitKey(0)