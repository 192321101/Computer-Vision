import cv2
import numpy as np
from google.colab.patches import cv2_imshow # Import cv2_imshow for Colab compatibility

image_path = "Ex12.jpg" # Corrected path for Colab environment
img = cv2.imread(image_path)

if img is None:
    print(f"Error: Image '{image_path}' not found. Please ensure the image is uploaded to the Colab environment.")
else:
    rows, cols = img.shape[:2]

    src_points = np.float32([[0,0],
                             [cols-1,0],
                             [0,rows-1],
                             [cols-1,rows-1]])

    dst_points = np.float32([[0,0],
                             [cols-1,0],
                             [int(0.33*cols),rows-1],
                             [int(0.66*cols),rows-1]])

    M = cv2.getPerspectiveTransform(src_points, dst_points)

    perspective = cv2.warpPerspective(img, M, (cols, rows))

    print("Original Image:")
    cv2_imshow(img)
    print("Perspective Image:")
    cv2_imshow(perspective)

    cv2.imwrite("Perspective_Transformed.jpg", perspective)

    # Removed cv2.waitKey(0) and cv2.destroyAllWindows() as they are not supported in Colab
