import cv2
from google.colab.patches import cv2_imshow

img = cv2.imread("Ex3.jpg") # Corrected path for Colab environment

if img is None:
    print("Error: Image 'Ex3.jpg' not found. Please ensure the image is uploaded to the Colab environment (e.g., to the /content/ directory).")
else:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    edges = cv2.Canny(gray, 100, 200)

    cv2_imshow(img)
    cv2_imshow(edges)

    cv2.imwrite("Canny_Edges.jpg", edges)
