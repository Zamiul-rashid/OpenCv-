import cv2 as cv 

cap = cv.VideoCapture(0)
haar_cascade = cv.CascadeClassifier(r'E:\OpenCv\Face_detection\har_cascade_face.xml')

while True:
    flag , frame  = cap.read()
    gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)#converting the BGR to grayscale 
    face_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=15)
    
    for x,y,w,h in face_rect:
        cv.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), thickness=2)
    cv.imshow("frame",frame)#showing in gray scale 
    if cv.waitKey(1) & 0xFF == ord("q"):
        break
    
cap.release()
cv.destroyAllWindows()
