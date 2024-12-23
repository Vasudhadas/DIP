import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the image
image = cv2.imread('image.jpg')  # Replace with your image path

# Check if the image is loaded correctly
if image is None:
    print("Error: Image not found")
    exit()

# 1. Pixelation
def pixelate(image, pixel_size=10):
    # Get the dimensions of the image
    height, width = image.shape[:2]
    
    # Resize the image to smaller size, then upscale it to original size
    temp_image = cv2.resize(image, (width // pixel_size, height // pixel_size), interpolation=cv2.INTER_LINEAR)
    pixelated_image = cv2.resize(temp_image, (width, height), interpolation=cv2.INTER_NEAREST)
    
    return pixelated_image

# 2. Blurring (Gaussian Blur)
def blur_image(image, kernel_size=(15, 15)):
    return cv2.GaussianBlur(image, kernel_size, 0)

# 3. Add Noise (Gaussian Noise) - Increased noise
def add_noise(image):
    row, col, ch = image.shape
    mean = 0
    sigma = 50  # Increased noise by setting a higher sigma value
    gaussian_noise = np.random.normal(mean, sigma, (row, col, ch))
    noisy_image = np.uint8(np.clip(image + gaussian_noise, 0, 255))
    
    return noisy_image

# Apply pixelation
pixelated_image = pixelate(image, pixel_size=10)

# Apply blur
blurred_image = blur_image(image, kernel_size=(15, 15))

# Apply more noise
noisy_image = add_noise(image)

# Plot the results
plt.figure(figsize=(12, 10))

# Original Image
plt.subplot(2, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))  # Convert BGR to RGB for displaying
plt.title('Original Image')
plt.axis('off')

# Pixelated Image
plt.subplot(2, 2, 2)
plt.imshow(cv2.cvtColor(pixelated_image, cv2.COLOR_BGR2RGB))
plt.title('Pixelated Image')
plt.axis('off')

# Blurred Image
plt.subplot(2, 2, 3)
plt.imshow(cv2.cvtColor(blurred_image, cv2.COLOR_BGR2RGB))
plt.title('Blurred Image')
plt.axis('off')

# Noisy Image with Increased Noise
plt.subplot(2, 2, 4)
plt.imshow(cv2.cvtColor(noisy_image, cv2.COLOR_BGR2RGB))
plt.title('Noisy Image (More Noise)')
plt.axis('off')

plt.tight_layout()
plt.show()
