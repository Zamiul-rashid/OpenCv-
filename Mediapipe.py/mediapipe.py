import cv2 as cv 
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils

my_hands = mp.solutions.hands
hands = my_hands.Hands()

my_face_mesh = mp.solutions.face_mesh.FaceMesh()
mp_face_mesh = mp.solutions.face_mesh

my_sholder_pose = mp.solutions.pose.Pose()
mp_pose = mp.solutions.pose

# mp_drawing = mp.solutions.drawing_styles

cap = cv.VideoCapture(0)

# bul , frame = cap.read() 

while True :
    bul , frame = cap.read() 
    if not bul :
        break
    frame = cv.flip(frame , 1)
    frame_rgb = cv.cvtColor(frame , cv.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)
    
    if results.multi_hand_landmarks :
        for hand_landmarks in results.multi_hand_landmarks :
            mp_drawing.draw_landmarks(frame , hand_landmarks , my_hands.HAND_CONNECTIONS ,
                mp_drawing.DrawingSpec(color=(255,0,255) , thickness=2 , circle_radius=2) ,
                mp_drawing.DrawingSpec(color=(0,255,255) , thickness=2 , circle_radius=2))
    results = my_face_mesh.process(frame_rgb)
    
    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            # Draw landmarks with connections
            mp_drawing.draw_landmarks(frame, face_landmarks, mp_face_mesh.FACEMESH_TESSELATION,
                            mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=1, circle_radius=1),
                            mp_drawing.DrawingSpec(color=(255, 0, 0), thickness=1, circle_radius=1))
    results = my_sholder_pose.process(frame_rgb)
    if results.pose_landmarks:
            # results.pose_landmarks
            mp_drawing.draw_landmarks(frame,results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                            mp_drawing.DrawingSpec(color=(255, 255, 255), thickness=1, circle_radius=1),
                            mp_drawing.DrawingSpec(color=(255, 255,255), thickness=1, circle_radius=1))
    # frame = cv.cvtColor(frame , cv.COLOR_RGB2BGR)
    cv.imshow("frame" , frame)
    if cv.waitKey(1) & 0xFF == ord("q") :
        break


cap.release()
cv.destroyAllWindows()