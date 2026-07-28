import cv2
from matplotlib import pyplot as plt # Import matplotlib for image display

# Correct the image path to 'q7.jpg' as it's now uploaded to Colab
image_path = "q7.jpg"
img = cv2.imread(image_path, 0) # Load as grayscale

if img is None:
    print(f"Error: Could not load image from '{image_path}'. Please ensure the image is uploaded to Colab.")
else:
    # 4-bit Quantization
    quantized = (img // 16) * 16

    # Use matplotlib for displaying images in Colab instead of cv2.imshow
    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    plt.imshow(img, cmap='gray') # Display grayscale image
    plt.title("Original Grayscale Image")
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(quantized, cmap='gray')
    plt.title("Quantized Image")
    plt.axis('off')

    plt.show()

    # cv2.waitKey(0) and cv2.destroyAllWindows() are not needed when using matplotlib in Colab.
