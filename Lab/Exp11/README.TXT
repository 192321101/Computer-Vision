import cv2
import numpy as np
from google.colab.patches import cv2_imshow # Import cv2_imshow for Colab compatibility

image_path = "Ex11.jpg" # Corrected path for Colab environment
img = cv2.imread(image_path)

if img is None:
    print(f"Error: Image '{image_path}' not found. Please ensure the image is uploaded to the Colab environment.")
else:
    rows, cols = img.shape[:2]

    M = np.float32([[1, 0, 100],
                    [0, 1, 50]])

    affine_img = cv2.warpAffine(img, M, (cols, rows))

    print("Original Image:")
    cv2_imshow(img)
    print("Affine Transformation:")
    cv2_imshow(affine_img)

    cv2.imwrite("Affine_Transformed.jpg", affine_img)

    # Removed cv2.waitKey(0) and cv2.destroyAllWindows() as they are not supported in Colab
