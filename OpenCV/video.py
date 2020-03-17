import cv2
import time

a = 1
video = cv2.VideoCapture(0)
while True:
	a += 1
	check, frame = video.read()

	# time.sleep(3)
	cv2.imshow("Title", frame)
	key = cv2.waitKey(1)
	if key == ord('q'):
		break

print(a)
video.release()
cv2.destroyAllWindows()