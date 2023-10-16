import cv2

# Define the file path to your image
image_path = "C:/Users/kovig/OneDrive/Documents/exp 5 picture.jpg"

# Load the image
image = cv2.imread(image_path)

# Check if the image was loaded successfully
if image is not None:
    # Define the rotation angle in degrees (positive for clockwise, negative for counterclockwise)
    clockwise_angle = 30
    counterclockwise_angle = -30

    # Get the image's height and width
    height, width = image.shape[:2]

    # Calculate the rotation matrix
    center = (width // 2, height // 2)
    clockwise_rotation_matrix = cv2.getRotationMatrix2D(center, clockwise_angle, 1.0)
    counterclockwise_rotation_matrix = cv2.getRotationMatrix2D(center, counterclockwise_angle, 1.0)

    # Apply the rotation
    rotated_clockwise = cv2.warpAffine(image, clockwise_rotation_matrix, (width, height))
    rotated_counterclockwise = cv2.warpAffine(image, counterclockwise_rotation_matrix, (width, height))

    # Display the original and rotated images
    cv2.imshow("Original Image", image)
    cv2.imshow("Rotated Clockwise", rotated_clockwise)
    cv2.imshow("Rotated Counterclockwise", rotated_counterclockwise)

    # Wait for a key press and close the windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print(f"Failed to load the image from {image_path}")
