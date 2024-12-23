import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread("image.jpg")
img_rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
height,width=img_rgb.shape[:2]

quad1=img_rgb[:height//2,:width//2]
quad2=img_rgb[:height//2,width//2:]
quad3=img_rgb[height//2:,:width//2]
quad4=img_rgb[height//2:,width//2:]

plt.imshow(img_rgb)
plt.title("Orignal Image")
plt.axis("off")
plt.show()

plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.imshow(quad1)
plt.title("Quadrant 1")
plt.axis("off")

plt.subplot(1,2,2)
plt.imshow(quad2)
plt.title("Quadrant 2")
plt.axis("off")

plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.imshow(quad3)
plt.title("Quadrant 3")
plt.axis("off")

plt.subplot(1,2,2)
plt.imshow(quad4)
plt.title("Quadrant 4")
plt.axis("off")

plt.show()