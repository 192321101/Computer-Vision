import cv2

image = cv2.imread(r"C:\Users\DHRANI\OneDrive\Desktop\CV\Ex10.jpg")

cv2.imshow("Original Image", image)

cv2.moveWindow("Original Image", 500, 300)

cv2.waitKey(0)
cv2.destroyAllWindows()
