import cv2
import matplotlib.pyplot as plt

# Using the correct path for the image uploaded to Colab
img = cv2.imread('/content/Q02.jpg')

# Check if the image was loaded successfully
if img is None:
    print("Error: Image not loaded. Please ensure 'Q02.jpg' is in /content/.")
else:
    # Gaussian blur for sharpening
    blur = cv2.GaussianBlur(img, (7,7), 0)

    # Sharpening using addWeighted
    sharp = cv2.addWeighted(img, 1.5, blur, -0.5, 0)

    # Using Matplotlib to display images in Colab, as cv2.imshow does not work directly
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title("Original Image")
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(cv2.cvtColor(sharp, cv2.COLOR_BGR2RGB))
    plt.title("Improved Image (Sharpened)")
    plt.axis('off')

    plt.show()

    # cv2.imshow and cv2.waitKey are typically for local GUI applications,
    # and do not work in Colab notebooks.
