import cv2
from matplotlib import pyplot as plt # Import matplotlib for image display

# Correct the image path to 'q8.jpg' as it's now uploaded to Colab
image_path = "q8.jpg"
img = cv2.imread(image_path)

if img is None:
    print(f"Error: Could not load image from '{image_path}'. Please ensure the image is uploaded to Colab.")
else:
    # Remove Noise (make sure image is color if using Colored denoise)
    # If the image was loaded in grayscale, you might need to convert it or use fastNlMeansDenoising
    denoise = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)

    # Use matplotlib for displaying images in Colab instead of cv2.imshow
    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)) # Convert BGR to RGB for matplotlib
    plt.title("Original Noisy Image")
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(cv2.cvtColor(denoise, cv2.COLOR_BGR2RGB))
    plt.title("Denoised Image")
    plt.axis('off')

    plt.show()

    # cv2.waitKey(0) and cv2.destroyAllWindows() are not needed when using matplotlib in Colab.
