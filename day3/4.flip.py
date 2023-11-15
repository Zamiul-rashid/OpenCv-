import cv2 as cv 
import numpy as np 

img = cv.imread("E:\OpenCv\Assets\pic1.jpg")

flliped = cv.flip(img , -1 )

cv.imshow("Flipped", flliped)
cv.waitKey(0)