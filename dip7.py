import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the image
image = cv2.imread('image.jpg')  # Replace with your image path

# Define transformations
tx, ty = 15, 30
angle, scale = 45, 1.2

# Translation (shift image by tx and ty)
M_translate = np.float32([[1, 0, tx], [0, 1, ty]])
translated_image = cv2.warpAffine(image, M_translate, (image.shape[1], image.shape[0]), borderValue=(255, 255, 255))

# Rotation (rotate by an angle and scale factor)
M_rotate = cv2.getRotationMatrix2D((image.shape[1] // 2, image.shape[0] // 2), angle, scale)
rotated_image = cv2.warpAffine(image, M_rotate, (image.shape[1], image.shape[0]), borderValue=(255, 255, 255))

# Scaling (resize image by scale factor)
scaled_image = cv2.resize(image, (int(image.shape[1] * scale), int(image.shape[0] * scale)), interpolation=cv2.INTER_LINEAR)

# Display images
titles = ['Original', 'Translated', 'Rotated', 'Scaled']
images = [image, translated_image, rotated_image, scaled_image]

plt.figure(figsize=(10, 10))
for i, img in enumerate(images):
    plt.subplot(2, 2, i + 1)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title(titles[i])
    plt.axis('off')

plt.tight_layout()
plt.show()
