import cv2
import numpy as np

# Read the image
image = cv2.imread("C:/Users/kovig/OneDrive/Documents/exp 21 picture.jpeg")

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Define the gradient masks
horizontal_gradient = np.array([[-1, -2, -1],
                                [0, 0, 0],
                                [1, 2, 1]], dtype=np.float32)

vertical_gradient = np.array([[-1, 0, 1],
                              [-2, 0, 2],
                              [-1, 0, 1]], dtype=np.float32)

# Calculate gradients in horizontal and vertical directions
gradient_x = cv2.filter2D(gray_image, -1, horizontal_gradient)
gradient_y = cv2.filter2D(gray_image, -1, vertical_gradient)

# Combine gradients to enhance edges
sharpened_image = cv2.addWeighted(gradient_x, 0.5, gradient_y, 0.5, 0)

# Convert the sharpened image back to BGR format
sharpened_image = cv2.cvtColor(sharpened_image, cv2.COLOR_GRAY2BGR)

# Display the original and sharpened images
cv2.imshow('Original Image', image)
cv2.imshow('Sharpened Image', sharpened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the sharpened image to a file
cv2.imwrite('sharpened_image.jpg', sharpened_image)
