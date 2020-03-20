import cv2
import time

first_frame = None

video = cv2.VideoCapture(0)
while True:
	check, frame = video.read()
	# gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	if first_frame is None:
		first_frame = frame
		# first_frame = gray

	cv2.imshow("Title", frame)
	# cv2.imshow("Title", gray)
	key = cv2.waitKey(1/10)
	if key == ord('q'):
		break

video.release()
cv2.destroyAllWindows()