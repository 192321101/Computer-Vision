import cv2
import numpy as np
from google.colab.patches import cv2_imshow

img = cv2.imread("Ex4.jpg", cv2.IMREAD_GRAYSCALE) # Corrected path for Colab environment

if img is None:
    print("Error: Image 'Ex4.jpg' not found. Please ensure the image is uploaded to the Colab environment (e.g., to the /content/ directory).")
else:
    kernel = np.ones((5,5), np.uint8)

    dilated_img = cv2.dilate(img, kernel, iterations=1)

    cv2_imshow(img)
    cv2_imshow(dilated_img)

    cv2.imwrite("Dilated_Image.jpg", dilated_img)
