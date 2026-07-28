import cv2
import matplotlib.pyplot as plt

# Using the correct path for the image uploaded to Colab
img = cv2.imread('/content/Q09.jpg')

# Check if the image was loaded successfully
if img is None:
    print("Error: Image not loaded. Please ensure 'Q09.jpg' is in /content/.")
else:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150)

    # Using Matplotlib to display images in Colab, as cv2.imshow does not work directly
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)) # Convert BGR to RGB for matplotlib
    plt.title("Original Image")
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(edges, cmap='gray')
    plt.title("Lane Detection (Canny Edges)")
    plt.axis('off')

    plt.show()

    # cv2.imshow and cv2.waitKey are typically for local GUI applications,
    # and do not work in Colab notebooks.
