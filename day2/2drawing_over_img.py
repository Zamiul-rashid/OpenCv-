import cv2 as cv 
import numpy as np 

blank = np.zeros((500,500,3),dtype="uint8")

#to paint a image a certain color 

blank[:]=255,0,0

"""[:] means all the pixels and we can also 
show specific areas by specifying the resolution"""

rectangle = cv.rectangle(blank,(0,0),(250,250),(0,0,250),thickness=2)
# #cv.rectangle(name , origin(tuple) , border_res(tuple) , color(BGR) , thickness= ? xb)


# #Circle 
circle = cv.circle(blank,(250,250),50,(0,255,0),thickness=2)
# #cv.circle(name , centre(tuple) , radius, color(BGR) , thickness= ? xb)

#adding text 
text = cv.putText(blank,"Hello",(0,150),cv.FONT_HERSHEY_PLAIN,1.0,(155,0,0),2)

# cv.imshow("blank",blank)
cv.imshow("border",text)

cv.waitKey(0)

cv.destroyAllWindows()

