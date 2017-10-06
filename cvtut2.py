import cv2
import numpy as np

#capturing video

cap = cv2.VideoCapture(0)

w = int(cap.get(3))	#3=frame width
h = int(cap.get(4))	#4=frame height

fourcc = cv2.VideoWriter_fourcc(*'MJPG')

out = cv2.VideoWriter('output.avi',fourcc, 20.0,(w,h))   #writing to file


while True:
	ret,frame = cap.read()
	gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	try:
        	out.write(frame)
	except:
        	print ('ERROR - Not writting to file')
	cv2.imshow('frame',frame)
	cv2.imshow('gray video',gray)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
out.release()
cv2.destroyAllWindows()