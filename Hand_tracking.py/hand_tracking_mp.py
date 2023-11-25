import cv2 as cv 
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
my_hands = mp.solutions.hands
# mp_drawing = mp.solutions.drawing_styles

cap = cv.VideoCapture(0)

bul , frame = cap.read() 

while True :
    bul , frame = cap.read() 
    if not bul :
        break
    frame = cv.flip(frame , 1)
    frame_rgb = cv.cvtColor(frame , cv.COLOR_BGR2RGB)
    results = my_hands.Hands().process(frame_rgb)
    if results.multi_hand_landmarks :
        for hand_landmarks in results.multi_hand_landmarks :
            mp_drawing.draw_landmarks(frame , hand_landmarks , my_hands.HAND_CONNECTIONS ,
                mp_drawing.DrawingSpec(color=(255,0,0) , thickness=2 , circle_radius=2) ,
                mp_drawing.DrawingSpec(color=(0,255,0) , thickness=2 , circle_radius=2))
    cv.imshow("frame" , frame)
    if cv.waitKey(1) & 0xFF == ord("q") :
        break


cap.release()
cv.destroyAllWindows()