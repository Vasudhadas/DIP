import cv2
import numpy as np
import matplotlib.pyplot as plt
 # Filters
low_pass_kernel = np.ones((5, 5), np.float32) / 25
high_pass_kernel = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]], np.float32)
 # Filter application function for color images
def apply_filter_color(image, kernel):
    channels = cv2.split(image)
    filtered_channels = [cv2.filter2D(channel, -1, kernel) for channel in channels]
    return cv2.merge(filtered_channels)
 # Load image and apply filters
image = cv2.imread('image.jpg')
low_pass_image = apply_filter_color(image, low_pass_kernel)
high_pass_image = apply_filter_color(image, high_pass_kernel)
band_pass_image = cv2.addWeighted(low_pass_image, 0.5, high_pass_image, 0.5, 0)
 # Convert BGR to RGB for Matplotlib
images = [cv2.cvtColor(img, cv2.COLOR_BGR2RGB) for img in [image, low_pass_image, high_pass_image, band_pass_image]]
titles = ['Original Image', 'Low-Pass Filter', 'High-Pass Filter', 'Band-Pass Filter']
 # Display results
plt.figure(figsize=(15, 5))
for i, img in enumerate(images):
    plt.subplot(1, 4, i + 1)
    plt.imshow(img)
    plt.title(titles[i])
    plt.axis('off')
plt.tight_layout()
plt.show()