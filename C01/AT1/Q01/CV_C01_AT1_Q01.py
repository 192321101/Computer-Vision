import cv2
from google.colab import files
import os

# IMPORTANT: You need to upload your image to Colab and update this path.
# Here's how you can do it:
# 1. Click on the folder icon on the left sidebar in Colab.
# 2. Click on the 'Upload to session storage' icon (looks like an arrow pointing up).
# 3. Select your image file (e.g., 'q1.jpg').
# 4. Once uploaded, use its name directly as the path.

# For example, if you upload 'q1.jpg':
image_path = "q1.jpg" # <--- Update this line after uploading your image!

# Alternatively, you can use files.upload() directly in a code cell:
# uploaded = files.upload()
# if uploaded:
#     image_path = list(uploaded.keys())[0]
#     print(f"Image '{image_path}' uploaded successfully.")
# else:
#     image_path = None
#     print("No image uploaded.")

img = cv2.imread(image_path)

if img is None:
    print(f"Error: Could not load image from '{image_path}'.\nPlease ensure you have uploaded the image to Colab and the 'image_path' variable is correct.")
else:
    small = cv2.resize(img, (100, 100), interpolation=cv2.INTER_NEAREST)

    sampled = cv2.resize(small, (img.shape[1], img.shape[0]),
                         interpolation=cv2.INTER_NEAREST)

    corrected = cv2.resize(small, (img.shape[1], img.shape[0]),
                           interpolation=cv2.INTER_CUBIC)

    # In Colab, cv2.imshow does not work directly as it requires a graphical display.
    # You'll need to convert the images to a format that can be displayed in the notebook.
    # For displaying images in Colab, use matplotlib or cv2_imshow from google.colab.patches.
    # Let's use matplotlib for demonstration.
    from matplotlib import pyplot as plt

    plt.figure(figsize=(15, 5))

    plt.subplot(1, 3, 1)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title("Original Image")
    plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.imshow(cv2.cvtColor(sampled, cv2.COLOR_BGR2RGB))
    plt.title("Improper Sampling")
    plt.axis('off')

    plt.subplot(1, 3, 3)
    plt.imshow(cv2.cvtColor(corrected, cv2.COLOR_BGR2RGB))
    plt.title("Corrected Image")
    plt.axis('off')

    plt.show()

    # The cv2.waitKey(0) and cv2.destroyAllWindows() are not needed for matplotlib display in Colab.
    # If you were running this on a local machine with a graphical environment, they would pause the display.
