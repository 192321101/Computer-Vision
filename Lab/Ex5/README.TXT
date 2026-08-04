import cv2
import numpy as np
from google.colab.patches import cv2_imshow

img = cv2.imread("Ex5.jpg") # Corrected path for Colab environment

if img is None:
    print("Error: Image 'Ex5.jpg' not found. Please ensure the image is uploaded to the Colab environment (e.g., to the /content/ directory).")
else:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))

    eroded = cv2.erode(gray, kernel, iterations=1)

    cv2_imshow(img)
    cv2_imshow(eroded)

    cv2.imwrite("eroded_image.jpg", eroded)
