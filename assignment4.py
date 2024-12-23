import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the grayscale image
image = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)  # Replace 'image.jpg' with your image path

# Check if the image is loaded correctly
if image is None:
    print("Error: Image not found")
    exit()

# Compute the histogram
histogram = cv2.calcHist([image], [0], None, [256], [0, 256])

# Plot the histogram
plt.figure(figsize=(10, 6))
plt.title('Grayscale Histogram')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')
plt.plot(histogram, color='black')
plt.xlim([0, 256])
plt.show()
