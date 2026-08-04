import cv2

img = cv2.imread("Ex1.jpg") # Corrected path to the image

if img is None:
    print("Error: Image 'Ex1.jpg' not found. Please make sure the image is uploaded to the Colab environment (e.g., to the /content/ directory if not using a specific path).")
else:
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cv2.imshow("Original Image", img)
    cv2.imshow("Grayscale Image", gray_img)

    cv2.imwrite("gray_image.jpg", gray_img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
