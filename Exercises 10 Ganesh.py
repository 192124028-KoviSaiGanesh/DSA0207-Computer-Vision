import cv2
import numpy as np

# Load the image
image = cv2.imread("C:/Users/kovig/OneDrive/Documents/exp 8 picture.png")

# Set the initial position of the image
initial_x, initial_y = 100, 100

# Set the target position where you want to move the image
target_x, target_y = 300, 300

# Create a VideoWriter to save the animation as a video (optional)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('image_animation.avi', fourcc, 30, (image.shape[1], image.shape[0]))

# Create a loop to animate the image movement
for step in range(100):  # Change the number of steps as needed
    # Calculate the intermediate position
    x = initial_x + (target_x - initial_x) * step / 100
    y = initial_y + (target_y - initial_y) * step / 100

    # Create a copy of the original image
    animated_image = image.copy()

    # Draw the image at the current position
    cv2.imshow("Image Animation", animated_image)
    cv2.moveWindow("Image Animation", int(x), int(y))

    # Save the frame to the video (optional)
    out.write(animated_image)

    if cv2.waitKey(30) & 0xFF == 27:  # Press 'Esc' key to exit
        break

# Release the VideoWriter (optional)
out.release()

# Close all windows
cv2.destroyAllWindows()
