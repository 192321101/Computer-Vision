import cv2
import matplotlib.pyplot as plt

# Using the correct path for the image uploaded to Colab
img = cv2.imread('/content/Q06.jpg')

# Check if the image was loaded successfully
if img is None:
    print("Error: Image not loaded. Please ensure 'Q06.jpg' is in /content/.")
else:
    small = cv2.resize(img, (300,300))
    gray = cv2.cvtColor(small, cv2.COLOR_BGR2GRAY)

    # Using Matplotlib to display images in Colab, as cv2.imshow does not work directly
    plt.figure(figsize=(15, 5))

    plt.subplot(1, 3, 1)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)) # Convert BGR to RGB for matplotlib
    plt.title("Original Image")
    plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.imshow(cv2.cvtColor(small, cv2.COLOR_BGR2RGB))
    plt.title("Reduced Resolution")
    plt.axis('off')

    plt.subplot(1, 3, 3)
    plt.imshow(gray, cmap='gray')
    plt.title("Grayscale Image")
    plt.axis('off')

    plt.show()

    # cv2.imshow and cv2.waitKey are typically for local GUI applications,
    # and do not work in Colab notebooks.
