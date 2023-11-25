import cv2 as cv 
import numpy as np 

img = cv.imread("E:\OpenCv\Assets\pic1.jpg")
cv.imshow("image", img)

def translation(img ,x,y):
    trasnmat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1],img.shape[0])
    
    return cv.warpAffine(img , trasnmat,dimensions)

transled = translation(img , -100 , 100)

# cv.imshow("translated",transled)

#Rotation of an image
def rotate(img , angle , rotateing_point = None ):
    (height , width) = img.shape[:2]
    
    if rotateing_point is None:
        rotateing_point= (width//2,height//2)
    
    rotateMat = cv.getRotationMatrix2D(rotateing_point , angle  , 1.0)
    dimension = (width,height)
    
    return cv.warpAffine(img , rotateMat, dimension) 


rotated = rotate(img,45) 
cv.imshow("img",rotated)   
    
    
cv.waitKey(0)

cv.destroyAllWindows()