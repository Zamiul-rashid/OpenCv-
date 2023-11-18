import cv2 as cv
img = cv.imread("E:\OpenCv\Assets\pic1.jpg")

cv.imshow('img', img)

#Average method 
blur1 = cv.blur(img , (7 ,7 ))
cv.imshow("Blur avg" , blur1)

#gaussiean blur 
blur2 = cv.GaussianBlur(img ,(7,7) ,0)
cv.imshow("Gaussian blur" , blur2)

#median blur 

blur3 = cv.medianBlur(img , 7)
cv.imshow("median blur" , blur3)


cv.waitKey(0)