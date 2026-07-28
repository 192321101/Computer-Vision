import cv2
from matplotlib import pyplot as plt # Import matplotlib for image display

# Correct the image path to 'q3.jpg' as it's now uploaded to Colab
image_path = "q3.jpg"
img = cv2.imread(image_path)

if img is None:
    print(f"Error: Could not load image from '{image_path}'. Please ensure the image is uploaded to Colab.")
else:
    small = cv2.resize(img, (120, 120))

    alias = cv2.resize(small,
                       (img.shape[1], img.shape[0]),
                       interpolation=cv2.INTER_NEAREST)

    filtered = cv2.GaussianBlur(alias, (5, 5), 0)

    # Use matplotlib for displaying images in Colab instead of cv2.imshow
    plt.figure(figsize=(15, 5))

    plt.subplot(1, 3, 1)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)) # Convert BGR to RGB for matplotlib
    plt.title("Original Image")
    plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.imshow(cv2.cvtColor(alias, cv2.COLOR_BGR2RGB))
    plt.title("Aliased Image")
    plt.axis('off')

    plt.subplot(1, 3, 3)
    plt.imshow(cv2.cvtColor(filtered, cv2.COLOR_BGR2RGB))
    plt.title("Filtered Image")
    plt.axis('off')

    plt.show()

    # cv2.waitKey(0) and cv2.destroyAllWindows() are not needed when using matplotlib in Colab.
