import cv2

# Load the images
img1 = cv2.imread("C:/Users/kovig/OneDrive/Documents/exp 2 picture.jpg")
img2 = cv2.imread("C:/Users/kovig/OneDrive/Documents/exp 3 picture.jpg")

# Crop the first image
(x1, y1) = (100, 100)
(x2, y2) = (300, 300)
cropped_img1 = img1[y1:y2, x1:x2]

# Copy the cropped image
copied_img1 = cropped_img1.copy()

# Paste the cropped image into the second image
(x, y) = (100, 100)
img2[y:y + copied_img1.shape[0], x:x + copied_img1.shape[1]] = copied_img1

# Display the output image
cv2.imshow("Output Image", img2)
cv2.waitKey(0)
