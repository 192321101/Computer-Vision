import cv2

img = cv2.imread(r"C:\Users\DHRANI\OneDrive\Desktop\CV\Ex9.jpg")

clockwise = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

counter = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

cv2.imshow("Original Image", img)
cv2.imshow("Clockwise Rotation", clockwise)
cv2.imshow("Counter Clockwise Rotation", counter)

cv2.imwrite("Clockwise.jpg", clockwise)
cv2.imwrite("CounterClockwise.jpg", counter)

cv2.waitKey(0)
cv2.destroyAllWindows()
