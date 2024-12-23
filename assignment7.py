import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the color image
image = cv2.imread('image.jpg')  # Replace with your image path

# Check if the image is loaded correctly
if image is None:
    print("Error: Image not found")
    exit()

# Convert the image from BGR to RGB (OpenCV uses BGR by default)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Split the image into R, G, and B channels
r, g, b = cv2.split(image_rgb)

# Apply histogram equalization to each channel
r_equalized = cv2.equalizeHist(r)
g_equalized = cv2.equalizeHist(g)
b_equalized = cv2.equalizeHist(b)

# Merge the equalized channels back together
equalized_image = cv2.merge((r_equalized, g_equalized, b_equalized))

# Plot the original and equalized images
plt.figure(figsize=(12, 6))

# Original Image
plt.subplot(1, 2, 1)
plt.imshow(image_rgb)
plt.title('Original Image')
plt.axis('off')

# Equalized Image
plt.subplot(1, 2, 2)
plt.imshow(equalized_image)
plt.title('Equalized Image')
plt.axis('off')

plt.tight_layout()
plt.show()
