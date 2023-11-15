import cv2 as cv 
img = cv.imread("E:\OpenCv\Assets\pic1.jpg")

# imread is the method for reading image and the ints (0,1,-1) are
# they are for the color grayscale and alpha channels 

cv.imshow("image",img)

#showing and craeting windows 

#wait time 
cv.waitKey(4999)# to make the imaage stick and the time is in micro seconds 

cv.destroyAllWindows()