import cv2
import numpy as np
from google.colab.patches import cv2_imshow # Import cv2_imshow for Colab compatibility

image_path = "Ex14.jpg" # Corrected path for Colab environment
img = cv2.imread(image_path)

if img is None:
    print(f"Error: Image '{image_path}' not found. Please ensure the image is uploaded to the Colab environment.")
else:
    rows, cols = img.shape[:2]

    src = np.float32([[0,0],
                      [cols-1,0],
                      [0,rows-1],
                      [cols-1,rows-1]])

    dst = np.float32([[0,0],
                      [cols-1,0],
                      [0,int(rows*0.7)],
                      [cols-1,int(rows*0.7)]])

    H, status = cv2.findHomography(src, dst)

    output = cv2.warpPerspective(img, H, (cols, rows))

    print("Original Image:")
    cv2_imshow(img) # Replaced cv2.imshow with cv2_imshow
    print("Homography Image:")
    cv2_imshow(output) # Replaced cv2.imshow with cv2_imshow

    cv2.imwrite("Homography_Image.jpg", output)

    # Removed cv2.waitKey(0) and cv2.destroyAllWindows() as they are not supported in Colab
