#translate 
import cv2 as cv 
import numpy as np 

img = cv.imread(".\Assets\pic2.jpg")
img = cv.resize(img,(700,700))
img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
img = cv.Canny(img,150,150)
cv.imshow("img",img)
cv.waitKey()
cv.destroyAllWindows()