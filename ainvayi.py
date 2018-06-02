import numpy as np
import cv2

# load the image
image = cv2.imread("/home/avani/Desktop/dogs.jpg")


for alpha in np.arange(0, 1.1, 0.1):
	# create two copies of the original image -- one for
	# the overlay and one for the final output image
	overlay = image.copy()
	output = image.copy()

	cv2.rectangle(overlay, (420, 205), (595, 385),(0, 0, 255), -1)
	#cv2.putText(overlay, "PyImageSearch: alpha={}".format(alpha),(10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 3)

	cv2.addWeighted(overlay, alpha, output, 1 - alpha,0, output)

	#print("alpha={}, beta={}".format(alpha, 1 - alpha))
	cv2.imshow("Output", output)
	cv2.waitKey(0)
