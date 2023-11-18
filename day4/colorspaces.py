import cv2 as cv 
img = cv.imread("E:\OpenCv\Assets\pic1.jpg")

cv.imshow("img" , img )

gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)

cv.imshow("Gray",gray)


cv.waitKey(0)
