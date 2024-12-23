import cv2
import numpy as np
import matplotlib.pyplot as plt

def enhance_and_segment(image_path):
    image=cv2.imread(image_path,cv2.IMREAD_GRAYSCALE)

    if image is None:
        print("Image not found or could not be loaded")
        return
    
    enhanced_image=cv2.equalizeHist(image)
    _,segmented_image=cv2.threshold(enhanced_image,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    plt.figure(figsize=(15,5))

    plt.subplot(1,3,1)
    plt.title("Original Image")
    plt.imshow(image,cmap='gray')
    plt.axis('off')

    plt.subplot(1,3,2)
    plt.title("Enhanced Image")
    plt.imshow(enhanced_image,cmap='gray')
    plt.axis('off')

    plt.subplot(1,3,3)
    plt.title("Segmented Image")
    plt.imshow(segmented_image,cmap='gray')
    plt.axis('off')

    plt.tight_layout()
    plt.show()

image_path='image.jpg'
enhance_and_segment(image_path)