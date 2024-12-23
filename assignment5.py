import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the image
image = cv2.imread('image.jpg')  # Replace with your image path

# Check if the image is loaded correctly
if image is None:
    print("Error: Image not found")
    exit()

# Convert to negative by subtracting pixel values from 255
negative_image = 255 - image

# Display the original and negative images
plt.figure(figsize=(10, 5))

# Original Image
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))  # Convert BGR to RGB for displaying
plt.title('Original Image')
plt.axis('off')

# Negative Image
plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(negative_image, cv2.COLOR_BGR2RGB))  # Convert BGR to RGB for displaying
plt.title('Negative Image')
plt.axis('off')

plt.tight_layout()
plt.show()
