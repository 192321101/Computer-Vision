import cv2
import matplotlib.pyplot as plt

# Using the correct path for the image uploaded to Colab (assuming q10.jpg exists)
img = cv2.imread('/content/q10.jpg')

# Check if the image was loaded successfully
if img is None:
    print("Error: Image not loaded. Please ensure 'q10.jpg' is in /content/.")
else:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    details = cv2.Laplacian(gray, cv2.CV_64F) # cv2.CV_64F to allow negative values from Laplacian

    # Using Matplotlib to display images in Colab, as cv2.imshow does not work directly
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)) # Convert BGR to RGB for matplotlib
    plt.title("Original Image")
    plt.axis('off')

    plt.subplot(1, 2, 2)
    # For displaying Laplacian output, often it's helpful to normalize or scale it for visualization
    # Since it's CV_64F, it can have negative values. Normalize to 0-255 for display.
    plt.imshow(details, cmap='gray', vmin=details.min(), vmax=details.max())
    plt.title("Fine Details (Laplacian)")
    plt.axis('off')

    plt.show()

    # cv2.imshow and cv2.waitKey are typically for local GUI applications,
    # and do not work in Colab notebooks.
