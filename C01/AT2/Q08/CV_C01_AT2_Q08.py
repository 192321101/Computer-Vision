import cv2
import matplotlib.pyplot as plt

# Using the correct path for the image uploaded to Colab
img = cv2.imread('/content/Q08.jpg', 0) # Read as grayscale directly

# Check if the image was loaded successfully
if img is None:
    print("Error: Image not loaded. Please ensure 'Q08.jpg' is in /content/.")
else:
    quantized = (img // 32) * 32

    # Using Matplotlib to display images in Colab, as cv2.imshow does not work directly
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.imshow(img, cmap='gray')
    plt.title("Original Medical Image")
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(quantized, cmap='gray')
    plt.title("Quantized Image")
    plt.axis('off')

    plt.show()

    # cv2.imshow and cv2.waitKey are typically for local GUI applications,
    # and do not work in Colab notebooks.
