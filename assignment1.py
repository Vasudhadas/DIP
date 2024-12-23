import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the image in RGB format
image = cv2.imread('image.jpg')  # Replace with your image path
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert to RGB (OpenCV loads in BGR by default)

# Convert the RGB image to Grayscale
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Extract individual R, G, B channels
r_channel = image_rgb[:, :, 0]  # Red channel
g_channel = image_rgb[:, :, 1]  # Green channel
b_channel = image_rgb[:, :, 2]  # Blue channel

# Display the images
plt.figure(figsize=(12, 10))

# Original RGB Image
plt.subplot(2, 3, 1)
plt.imshow(image_rgb)
plt.title('Original RGB Image')
plt.axis('off')

# Grayscale Image
plt.subplot(2, 3, 2)
plt.imshow(image_gray, cmap='gray')
plt.title('Grayscale Image')
plt.axis('off')

# Red Channel
plt.subplot(2, 3, 3)
plt.imshow(r_channel, cmap='Reds')
plt.title('Red Channel')
plt.axis('off')

# Green Channel
plt.subplot(2, 3, 4)
plt.imshow(g_channel, cmap='Greens')
plt.title('Green Channel')
plt.axis('off')

# Blue Channel
plt.subplot(2, 3, 5)
plt.imshow(b_channel, cmap='Blues')
plt.title('Blue Channel')
plt.axis('off')

plt.tight_layout()
plt.show()
