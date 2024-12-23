import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the image
image = cv2.imread('image.jpg')  # Replace with your image path
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert to RGB (OpenCV loads in BGR by default)

# Separate the R, G, B channels
r_channel = image_rgb[:, :, 0]
g_channel = image_rgb[:, :, 1]
b_channel = image_rgb[:, :, 2]

# Calculate histograms for each channel
r_hist = cv2.calcHist([r_channel], [0], None, [256], [0, 256])
g_hist = cv2.calcHist([g_channel], [0], None, [256], [0, 256])
b_hist = cv2.calcHist([b_channel], [0], None, [256], [0, 256])

# Plot the histograms
plt.figure(figsize=(12, 6))

# Red channel histogram
plt.subplot(1, 3, 1)
plt.plot(r_hist, color='red')
plt.title('Red Channel Histogram')
plt.xlim([0, 256])

# Green channel histogram
plt.subplot(1, 3, 2)
plt.plot(g_hist, color='green')
plt.title('Green Channel Histogram')
plt.xlim([0, 256])

# Blue channel histogram
plt.subplot(1, 3, 3)
plt.plot(b_hist, color='blue')
plt.title('Blue Channel Histogram')
plt.xlim([0, 256])

plt.tight_layout()
plt.show()
