import cv2

img = cv2.imread("galaxy.jpg", 0)

img = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))
cv2.imshow("Galaxy", img)
cv2.imwrite("Galaxy1.jpg", img)
cv2.waitKey(0)
cv2.destroyAllWindows()