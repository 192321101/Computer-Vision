import cv2
from matplotlib import pyplot as plt # Import matplotlib for image display

# Correct the image path to 'q10.jpg' as it's now uploaded to Colab
image_path = "q10.jpg"
img = cv2.imread(image_path)

if img is None:
    print(f"Error: Could not load image from '{image_path}'. Please ensure the image is uploaded to Colab.")
else:
    # Reduce Resolution
    low = cv2.resize(img, (64, 64))

    # Restore Image
    restored = cv2.resize(low,
                          (img.shape[1], img.shape[0]),
                          interpolation=cv2.INTER_CUBIC)

    # Use matplotlib for displaying images in Colab instead of cv2.imshow
    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)) # Convert BGR to RGB for matplotlib
    plt.title("Original Image")
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(cv2.cvtColor(restored, cv2.COLOR_BGR2RGB))
    plt.title("Low Resolution Image")
    plt.axis('off')

    plt.show()

    # cv2.waitKey(0) and cv2.destroyAllWindows() are not needed when using matplotlib in Colab.
