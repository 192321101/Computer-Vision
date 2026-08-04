import cv2
import numpy as np
from google.colab.patches import cv2_imshow # Import cv2_imshow for Colab compatibility

video_path = "Ex13.mp4" # Corrected path for Colab environment
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print(f"Error: Could not open video {video_path}. Please ensure the video is uploaded to the Colab environment.")
else:
    # Process only the first frame for display in Colab
    ret, frame = cap.read()

    if ret:
        rows, cols = frame.shape[:2]

        src = np.float32([[100,100],
                          [cols-100,100],
                          [100,rows-100],
                          [cols-100,rows-100]])

        dst = np.float32([[0,0],
                          [cols,0],
                          [100,rows],
                          [cols-100,rows]])

        M = cv2.getPerspectiveTransform(src, dst)

        output = cv2.warpPerspective(frame, M, (cols, rows))

        print("Original Video (First Frame):")
        cv2_imshow(frame) # Replaced cv2.imshow with cv2_imshow
        print("Perspective Video (First Frame):")
        cv2_imshow(output) # Replaced cv2.imshow with cv2_imshow
    else:
        print(f"Error: Could not read the first frame from {video_path}.")

cap.release()
# Removed cv2.destroyAllWindows() and cv2.waitKey() as they are not supported in Colab
