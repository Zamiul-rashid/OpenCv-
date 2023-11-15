import cv2 as cv 

cap = cv.VideoCapture(0)

while True:
    flag , frame  = cap.read()
    gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)#converting the BGR to grayscale 
    cv.imshow("frame",gray)#showing in gray scale 
    if cv.waitKey(1) & 0xFF == ord("q"):
        break
    
cap.release()
cv.destroyAllWindows()
