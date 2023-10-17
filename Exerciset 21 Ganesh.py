import cv2
import numpy as np

# Read the image
image = cv2.imread("C:/Users/kovig/OneDrive/Documents/exp 8 picture.png")

# Define the Laplacian mask with diagonal neighbors
laplacian_mask = np.array([[1, 1, 1],
                           [1, -8, 1],
                           [1, 1, 1]], dtype=np.float32)

# Apply the convolution with the Laplacian mask
sharpened_image = cv2.filter2D(image, -1, laplacian_mask)

# Add the result of the convolution to the original image
sharpened_image = cv2.add(image, sharpened_image)

# Display the original and sharpened images
cv2.imshow('Original Image', image)
cv2.imshow('Sharpened Image', sharpened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the sharpened image to a file
cv2.imwrite('sharpened_image.jpg', sharpened_image)
