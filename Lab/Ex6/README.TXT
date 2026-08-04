import cv2
from google.colab.patches import cv2_imshow

video_path = "Ex6.mp4"
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print(f"Error: Could not open video {video_path}. Please ensure the video is uploaded to the Colab environment.")
else:
    ret, frame = cap.read() # Read the first frame

    if ret:
        print("Displaying the first frame of the video:")
        slow = cv2.resize(frame, None, fx=0.5, fy=0.5)
        fast = cv2.resize(frame, None, fx=2.0, fy=2.0)

        print("Slow Motion (first frame):")
        cv2_imshow(slow)
        print("Fast Motion (first frame):")
        cv2_imshow(fast)
    else:
        print("Error: Could not read the first frame from the video.")

    cap.release()
