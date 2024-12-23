import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the image
image = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)

# Define the structuring element
kernel = np.ones((5, 5), np.uint8)

# Apply Erosion
eroded_image = cv2.erode(image, kernel, iterations=1)

# Subtract Eroded Image from Original
subtracted_erode = cv2.subtract(image, eroded_image)

# Apply Dilation
dilated_image = cv2.dilate(image, kernel, iterations=1)

# Subtract Dilated Image from Original and Normalize the Result
subtracted_dilate = cv2.subtract(dilated_image, image)
subtracted_dilate_normalized = cv2.normalize(subtracted_dilate, None, 0, 255, cv2.NORM_MINMAX)

# Plot results
plt.figure(figsize=(10, 8))
plt.subplot(2, 3, 1), plt.imshow(image, cmap='gray'), plt.title('Original Image')
plt.subplot(2, 3, 2), plt.imshow(eroded_image, cmap='gray'), plt.title('Eroded Image')
plt.subplot(2, 3, 3), plt.imshow(subtracted_erode, cmap='gray'), plt.title('Original - Eroded')
plt.subplot(2, 3, 4), plt.imshow(dilated_image, cmap='gray'), plt.title('Dilated Image')
plt.subplot(2, 3, 5), plt.imshow(subtracted_dilate_normalized, cmap='gray'), plt.title('Original - Dilated')
plt.tight_layout()
plt.show()
