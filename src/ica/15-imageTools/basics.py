from src.ica.helpers.imageTools import *
from src.ica.helpers.dummyWindow import *

# Load the mightyMidway image
pic = Picture("../SampleImages/mightyMidway.jpg")

# Get width and height
width = pic.getWidth()
height = pic.getHeight()

# Print the number of pixels
num_pixels = width * height
print("Number of pixels in mightyMidway.jpg:", num_pixels)

# Make a copy of the image
copy_pic = pic.copy()

# Define red color
red = (255, 0, 0)

# Set each corner pixel to red
copy_pic.setColor(0, 0, red)  # top-left
copy_pic.setColor(width - 1, 0, red)  # top-right
copy_pic.setColor(0, height - 1, red)  # bottom-left
copy_pic.setColor(width - 1, height - 1, red)  # bottom-right

# Save the new image
copy_pic.save("../SampleImages/mightyMidway-redCorners.jpg")

# Explore the new image
copy_pic.explore()

# Keep the window open
keep_windows_open()
