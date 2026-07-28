import cv2
from matplotlib import pyplot as plt # Import matplotlib for image display

# Correct the image path to 'q4.jpg' as it's now uploaded to Colab
image_path = "q4.jpg"
img = cv2.imread(image_path, 0)

if img is None:
    print(f"Error: Could not load image from '{image_path}'. Please ensure the image is uploaded to Colab.")
else:
    low_pixel = cv2.resize(img, (128, 128))
    low_pixel = cv2.resize(low_pixel,
                           (img.shape[1], img.shape[0]))

    quantized = (img // 32) * 32

    # Use matplotlib for displaying images in Colab instead of cv2.imshow
    plt.figure(figsize=(18, 6))

    plt.subplot(1, 3, 1)
    plt.imshow(img, cmap='gray') # Grayscale images can be displayed directly
    plt.title("Original Image")
    plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.imshow(low_pixel, cmap='gray')
    plt.title("Low Pixel Resolution")
    plt.axis('off')

    plt.subplot(1, 3, 3)
    plt.imshow(quantized, cmap='gray')
    plt.title("Reduced Intensity Resolution")
    plt.axis('off')

    plt.show()

    # cv2.waitKey(0) and cv2.destroyAllWindows() are not needed when using matplotlib in Colab.
