import cv2 as cv 

haar_cascade = cv.CascadeClassifier('E:\OpenCv\Face_detection\har_cascade_face.xml')
img_arrey = cv.imread(r"E:\OpenCv\Face_detection\samp2.jpg")
img_arrey = cv.resize(img_arrey, (500,500))
gray = cv.cvtColor(img_arrey, cv.COLOR_BGR2GRAY)

face_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=15)


for x,y,w,h in face_rect:
    cv.rectangle(img_arrey, (x,y), (x+w, y+h), (0,255,0), thickness=2)

cv.imshow('Person', img_arrey)
cv.waitKey(0)
