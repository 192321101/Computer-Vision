import cv2
from matplotlib import pyplot as plt

# The image 'q2.jpg' has been uploaded to the Colab environment.
image_path = "q2.jpg" # Corrected path to the uploaded image

img = cv2.imread(image_path)

if img is None:
    print(f"Error: Could not load image from '{image_path}'. Please ensure the image is uploaded.")
else:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    enhanced = cv2.equalizeHist(gray)

    plt.figure(figsize=(15, 5))

    plt.subplot(1, 3, 1)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)) # Convert BGR to RGB for matplotlib
    plt.title("Original Low-Light Image")
    plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.imshow(gray, cmap='gray') # Grayscale images can be displayed directly
    plt.title("Gray Image")
    plt.axis('off')

    plt.subplot(1, 3, 3)
    plt.imshow(enhanced, cmap='gray')
    plt.title("Enhanced Image")
    plt.axis('off')

    plt.show()

    # cv2.waitKey(0) and cv2.destroyAllWindows() are not needed when using matplotlib in Colab.
