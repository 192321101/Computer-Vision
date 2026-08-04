import cv2
from google.colab.patches import cv2_imshow # Import cv2_imshow for Colab compatibility

image_path = "Ex8.jpg" # Corrected path for Colab environment
image = cv2.imread(image_path)

if image is None:
    print(f"Error: Image '{image_path}' not found. Please ensure the image is uploaded to the Colab environment.")
else:
    height, width = image.shape[:2]

    bigger = cv2.resize(image, (int(width*3), int(height*3)))
    smaller = cv2.resize(image, (int(width*0.5), int(height*0.5)))

    print("Original Image:")
    cv2_imshow(image)
    print("Bigger Image:")
    cv2_imshow(bigger)
    print("Smaller Image:")
    cv2_imshow(smaller)

    cv2.imwrite("Bigger_Image.jpg", bigger)
    cv2.imwrite("Smaller_Image.jpg", smaller)

    # Removed cv2.waitKey(0) and cv2.destroyAllWindows() as they are not supported in Colab
