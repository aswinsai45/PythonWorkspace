import cv2

img = cv2.imread ("D:\\OpenCV_Practice\\Mom.jpg", 1)
resized = cv2.resize (img, (600, 400))
cv2.imshow ("Mom", resized)
cv2.waitKey (0)
cv2.destroyAllWindows ()
