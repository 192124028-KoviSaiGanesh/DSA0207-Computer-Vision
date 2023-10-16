import cv2

cap = cv2.VideoCapture("C:/Users/kovig/OneDrive/Documents/exp 6 video.mp4")

if not cap.isOpened():
    print("Error opening video file")

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break

    cv2.imshow('Frame', frame)

    if cv2.waitKey(250) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
