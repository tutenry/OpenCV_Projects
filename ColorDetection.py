import cv2
import numpy as np

cam = cv2.VideoCapture(0)

while True:
	available, frame = cam.read()

	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	lower_blue = np.array([100, 50, 50])
	upper_blue = np.array([130, 255, 255])

	mask = cv2.inRange(hsv, lower_blue, upper_blue)

	result = cv2.bitwise_and(frame, frame, mask = mask)


	cv2.imshow("OpenCV", result)
	

	if cv2.waitKey(1) == ord("q"):
		break

cam.release()
cv2.destroyAllWindows()