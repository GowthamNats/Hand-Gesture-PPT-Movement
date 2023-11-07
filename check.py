import os
import cv2

image_path = "d:\VIT\Semester 7\HCI\hci ppt\Presentation"

# Check if the image file exists.
if not os.path.exists(image_path):
    print("Image file does not exist.")
    exit()

# Load the image using OpenCV.
imgCurrent = cv2.imread(image_path)

# Check if the image was loaded successfully.
if imgCurrent is None:
    print("Image could not be loaded.")
    exit()

# Get the height, width, and channels of the image.
h, w, _ = imgCurrent.shape

# Print the height, width, and channels of the image.
print("Height:", h)
print("Width:", w)
print("Channels:", _)