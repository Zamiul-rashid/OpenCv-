import cv2 as cv 

img = cv.imread("E:\OpenCv\Assets\pic1.jpg")


def resize_shitz(frame , size = .80):
    #can be used for images videos and live videos 
    breath = int(frame.shape[0] *size)
    height = int(frame.shape[1] *size)
    
    dimension = (breath , height)
    
    return cv.resize(frame , dimension,interpolation= cv.INTER_AREA)
    #still a little confuded about the stntax and the interpolation part 

resized = resize_shitz(img,size= .50)

cv.imshow("Image",resized)
cv.waitKey(0)

cv.destroyAllWindows()