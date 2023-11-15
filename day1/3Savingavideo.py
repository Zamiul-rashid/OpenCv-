import cv2 as cv 

show = cv.VideoCapture(0)
frcc = cv.VideoWriter_fourcc(*"xvid")
temp = cv.VideoWriter("Printed video.avi",frcc,24.0,(640,480))
while True:
    flag , frame  = show.read()
    cv.imshow("frame",frame)#showing in gray scale 
    temp.write(frame)
    if cv.waitKey(1) & 0xFF == ord("q"):
        break
    
show.release()
temp.release()
cv.destroyAllWindows()