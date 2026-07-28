import cv2
import matplotlib.pyplot as plt

# Using the correct path for the image uploaded to Colab
img = cv2.imread('/content/Q01.jpg')

# Check if the image was loaded successfully
if img is None:
    print("Error: Image not loaded. Please ensure 'Q01.jpg' is in /content/.")
else:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ccd = cv2.GaussianBlur(gray, (5,5), 0)
    cmos = cv2.GaussianBlur(gray, (3,3), 2)

    # Using Matplotlib to display images in Colab, as cv2.imshow does not work directly
    plt.figure(figsize=(15, 5))

    plt.subplot(1, 3, 1)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title("Original Image")
    plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.imshow(ccd, cmap='gray')
    plt.title("CCD Image (GaussianBlur 5x5)")
    plt.axis('off')

    plt.subplot(1, 3, 3)
    plt.imshow(cmos, cmap='gray')
    plt.title("CMOS Image (GaussianBlur 3x3)")
    plt.axis('off')

    plt.show()

    # cv2.imshow and cv2.waitKey are typically for local GUI applications,
    # and do not work in Colab notebooks.
