import cv2
from google.colab import files
from google.colab.patches import cv2_imshow

# Upload image
uploaded = files.upload()

img = cv2.imread("q6.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Improve image quality
enhanced = cv2.equalizeHist(gray)

print("Original Image")
cv2_imshow(img)

print("Enhanced Image")
cv2_imshow(enhanced)
