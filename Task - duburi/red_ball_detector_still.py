import cv2 as cv
import numpy as np

# Specifying upper and lower ranges of color to detect in hsv format
lower = np.array([0, 100, 100])
upper = np.array([10, 255, 255])  # These ranges will detect red

# Loading the image
frame = cv.imread(r'E:\Task - duburi\images (3).jpeg')
# frame = cv.imread(r'E:\Task - duburi\unnamed.jpg')

img = cv.cvtColor(frame, cv.COLOR_BGR2HSV)  # Converting BGR image to HSV format
mask = cv.inRange(img, lower, upper)  # Masking the image to find the specified color
grey = cv.cvtColor(frame, cv.COLOR_BGR2GRAY) # Converting BGR image to greyscale format

mask_contours, hierarchy = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)  # Finding contours in mask image and taking the external coordinates

# Finding circles in the masked image
circle = cv.HoughCircles(grey , cv.HOUGH_GRADIENT, 1, 20, param1=50, param2=40 , minRadius=1, maxRadius=50)

if mask_contours is not None and circle is not None:
    count = 0;red_ball = 0
    mask_contours = sorted(mask_contours, key=cv.contourArea, reverse=True)[:3]  # Consider only the largest three contour
    circle = np.uint16(np.around(circle))  # Convert circle parameters to integer type
    for i in circle[0, :]:
            # Draw the outer circle
            cv.circle(frame, (i[0], i[1]), i[2], (0, 255, 0), 2)
            # Draw the center of the circle
            cv.circle(frame, (i[0], i[1]), 2, (255, 0, 255), 3)

    for mask_contour in mask_contours:
        if cv.contourArea(mask_contour) >20:
            x, y, w, h = cv.boundingRect(mask_contour)
            cv.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 1) # Drawing rectangle
            red_ball += 1
        count +=  1
    print(f"Number of
          \nred balls detected: {red_ball}")      
    print(f"Number of circles detected: {len(circle[0, :])}")
else:
    print("No cicle detected")           

cv.imshow("mask image", mask)  # Displaying mask image
cv.imshow("window", frame)  # Displaying the image with contours and circles

while True:
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cv.destroyAllWindows()
