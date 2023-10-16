import cv2

cap = cv2.VideoCapture(0)
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # Added missing closing parenthesis
fps = cap.get(cv2.CAP_PROP_FPS)
path = "C:/Users/kovig/OneDrive/Documents/exp 7 video.mp4"
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
output = cv2.VideoWriter(path, fourcc, fps, (width, height))

while True:
    ret, frame = cap.read()

    if not ret:
        break

    cv2.imshow("frame", frame)
    output.write(frame)

    k = cv2.waitKey(24)
    if k == ord('q'):
        break

cap.release()
output.release()
cv2.destroyAllWindows()
