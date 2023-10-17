import cv2
import numpy as np

# Read the image
image = cv2.imread("C:/Users/kovig/OneDrive/Documents/exp 23 picture.jpeg")

# Step 1: Create a blurred version of the original image
blurred_image = cv2.GaussianBlur(image, (0, 0), 3)

# Step 2: Create the unsharp mask
unsharp_mask = cv2.addWeighted(image, 2.5, blurred_image, -1.5, 0)

# Display the original image, blurred image, and unsharp masked image
cv2.imshow('Original Image', image)
cv2.imshow('Blurred Image', blurred_image)
cv2.imshow('Unsharp Masked Image', unsharp_mask)
cv2.waitKey(0)
cv2.destroyAllWindows()
