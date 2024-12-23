import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the colored image
image = cv2.imread('image.jpg')  # Replace with your image path
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert from BGR to RGB

# Linear Transformation (Apply on each channel)
def linear_transformation(image, alpha, beta):
    return cv2.convertScaleAbs(image, alpha=alpha, beta=beta)

# Gamma Transformation (Apply on each channel)
def gamma_transformation(image, gamma):
    image_normalized = image / 255.0  # Normalize image to [0, 1]
    gamma_corrected = np.power(image_normalized, gamma)  # Apply gamma correction
    return np.uint8(gamma_corrected * 255)  # Scale back to [0, 255]

# Logarithmic Transformation (Apply on each channel)
def logarithmic_transformation(image):
    # First, normalize the image to range [0, 1] by dividing by 255
    image_normalized = image / 255.0
    # Apply the logarithmic transformation
    log_image = np.log(1 + image_normalized)  # Logarithmic transformation
    # Scale back to [0, 255] and convert to uint8
    log_image = np.uint8(log_image * 255)
    return log_image

# Separate the R, G, B channels
r_channel = image_rgb[:, :, 0]
g_channel = image_rgb[:, :, 1]
b_channel = image_rgb[:, :, 2]

# Apply transformations on each channel
alpha, beta = 1.5, 50  # For linear transformation
gamma_value = 2.2  # For gamma transformation

r_linear = linear_transformation(r_channel, alpha, beta)
g_linear = linear_transformation(g_channel, alpha, beta)
b_linear = linear_transformation(b_channel, alpha, beta)

r_gamma = gamma_transformation(r_channel, gamma_value)
g_gamma = gamma_transformation(g_channel, gamma_value)
b_gamma = gamma_transformation(b_channel, gamma_value)

r_log = logarithmic_transformation(r_channel)
g_log = logarithmic_transformation(g_channel)
b_log = logarithmic_transformation(b_channel)

# Merge transformed channels back into RGB images
linear_image = cv2.merge([r_linear, g_linear, b_linear])
gamma_image = cv2.merge([r_gamma, g_gamma, b_gamma])
log_image = cv2.merge([r_log, g_log, b_log])

# Plot the results
plt.figure(figsize=(12, 10))

# Original Image
plt.subplot(2, 2, 1)
plt.imshow(image_rgb)
plt.title('Original Image')
plt.axis('off')

# Linear Transformation
plt.subplot(2, 2, 2)
plt.imshow(linear_image)
plt.title('Linear Transformation')
plt.axis('off')

# Gamma Transformation
plt.subplot(2, 2, 3)
plt.imshow(gamma_image)
plt.title(f'Gamma Transformation (gamma={gamma_value})')
plt.axis('off')

# Logarithmic Transformation
plt.subplot(2, 2, 4)
plt.imshow(log_image)
plt.title('Logarithmic Transformation')
plt.axis('off')

plt.tight_layout()
plt.show()
