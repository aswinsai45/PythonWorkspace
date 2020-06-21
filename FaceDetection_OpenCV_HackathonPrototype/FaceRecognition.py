import cv2

# Create a cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# reading the image
img = cv2.imread ("D:\\OpenCV_Practice\\Baby.jpg")
# Converting image to grayscale
gray = cv2.cvtColor (img, cv2.COLOR_BGR2GRAY)
# Searching coordinates of the image (Faces)
faces = face_cascade.detectMultiScale (gray, 1.05, 5)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h),(0, 165, 255), 3)

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

