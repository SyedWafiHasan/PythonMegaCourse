import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")

img = cv2.imread('p2.jpg')
# cv2.imwrite("ds_small.jpg", cv2.resize(img, (int(img.shape[1]/4), int(img.shape[0]/4))))

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=20)
print(faces)

for x, y, w, h in faces:
	img=cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)

cv2.imshow("Gray", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
