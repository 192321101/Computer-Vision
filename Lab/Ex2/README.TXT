import cv2
from google.colab.patches import cv2_imshow

image = cv2.imread("Ex2.jpg") # Corrected path for Colab environment

if image is None:
    print("Error: Image 'Ex2.jpg' not found. Please ensure the image is uploaded to the Colab environment (e.g., to the /content/ directory).")
else:
    blur = cv2.GaussianBlur(image, (5,5), 10)

    cv2_imshow(image)
    cv2_imshow(blur)

    cv2.imwrite("blurred_image.jpg", blur)
