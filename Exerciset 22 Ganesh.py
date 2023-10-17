import cv2
import numpy as np

# Read the image
image = cv2.imread("C:/Users/kovig/OneDrive/Documents/exp 21 picture.jpeg")

# Define the Laplacian mask with a positive center coefficient
laplacian_mask = np.array([[0, -1, 0],
                           [-1, 5, -1],
                           [0, -1, 0]], dtype=np.float32)

# Apply the convolution with the Laplacian mask
sharpened_image = cv2.filter2D(image, -1, laplacian_mask)

# Subtract the result of the convolution from the original image
sharpened_image = cv2.subtract(image, sharpened_image)

# Display the original and sharpened images
cv2.imshow('Original Image', image)
cv2.imshow('Sharpened Image', sharpened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the sharpened image to a file
cv2.imwrite('sharpened_image.jpg', sharpened_image)
