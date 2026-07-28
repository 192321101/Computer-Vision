import cv2
from matplotlib import pyplot as plt # Import matplotlib for image display

# Correct the image path to 'q5.jpg' as it's now uploaded to Colab
image_path = "q5.jpg"
img = cv2.imread(image_path)

if img is None:
    print(f"Error: Could not load image from '{image_path}'. Please ensure the image is uploaded to Colab.")
else:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    edges = cv2.Canny(gray, 100, 200)

    # Use matplotlib for displaying images in Colab instead of cv2.imshow
    plt.figure(figsize=(18, 6))

    plt.subplot(1, 3, 1)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)) # Convert BGR to RGB for matplotlib
    plt.title("Original Surveillance Image")
    plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.imshow(gray, cmap='gray') # Grayscale images can be displayed directly
    plt.title("Gray Image")
    plt.axis('off')

    plt.subplot(1, 3, 3)
    plt.imshow(edges, cmap='gray')
    plt.title("Detected Edges")
    plt.axis('off')

    plt.show()

    # cv2.waitKey(0) and cv2.destroyAllWindows() are not needed when using matplotlib in Colab.
