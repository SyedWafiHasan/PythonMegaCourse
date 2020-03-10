import cv2
import glob

images = glob.glob('*.jpg')

for i in images:
	img = cv2.imread(i, 1)
	img1 = cv2.resize(img, (100, 100))
	cv2.imshow("Oi Suzy", img)
	cv2.waitKey(500)
	cv2.destroyAllWindows()
	cv2.imwrite("resized_"+i, img1)