import cv2
# Read the original image
img = cv2.imread("C:/Users/kovig/OneDrive/Documents/exp 23 picture.jpeg")
cv2.imshow('Original', img)
cv2.waitKey(0)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Blur the image for better edge detection
img_blur = cv2.GaussianBlur(img_gray, (3,3), 0)

sobely = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5)

cv2.imshow('Sobel Y', sobely)
cv2.waitKey(0)
