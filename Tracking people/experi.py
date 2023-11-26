import cv2

# Read the video
video_path = r"E:\OpenCv\Tracking people\People Walking Past the Camera - Free Stock Footage For Commercial Projects.mp4"
cap = cv2.VideoCapture(video_path)

# Create a background subtractor
bg_subtractor = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=50, detectShadows=True)

# Create a CSRT tracker
tracker = cv2.TrackerCSRT_create()

# Read the first frame
ret, frame = cap.read()
if not ret:
    print("Error reading the video")
    exit()

# Define a region of interest (ROI) to track
bbox = cv2.selectROI("Frame", frame, fromCenter=False, showCrosshair=True)
tracker.init(frame, bbox)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Apply background subtraction
    fg_mask = bg_subtractor.apply(frame)

    # Update the tracker
    ret, bbox = tracker.update(frame)
    if ret:
        # Draw bounding box around the tracked object
        (x, y, w, h) = [int(i) for i in bbox]
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow('Frame', frame)
    # cv2.imshow('Foreground Mask', fg_mask)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
