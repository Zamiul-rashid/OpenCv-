import cv2 as cv
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
my_face_mesh = mp.solutions.face_mesh.FaceMesh()
mp_face_mesh = mp.solutions.face_mesh

cap = cv.VideoCapture(0)

while True:
    bul, frame = cap.read()
    if not bul:
        break
    frame = cv.flip(frame, 1)
    frame_rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    results = my_face_mesh.process(frame_rgb)
    
    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            # Draw landmarks with connections
            mp_drawing.draw_landmarks(frame, face_landmarks, mp_face_mesh.FACEMESH_TESSELATION,
                                      landmark_drawing_spec=mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=1, circle_radius=1),
                                      connection_drawing_spec=mp_drawing.DrawingSpec(color=(255, 0, 0), thickness=1, circle_radius=1)
                                      )
            # mp_drawing.draw_landmarks(frame,face_landmarks,mp.solutions.face_mesh.FACE_CONNECTIONS)
            

    cv.imshow("frame", frame)
    if cv.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv.destroyAllWindows()
