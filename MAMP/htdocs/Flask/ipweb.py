import urllib.request
import cv2
import numpy as np
import ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = 'http://10.12.1.211:8080/shot.jpg'
while True:
	imgResp = urllib.request.urlopen(url)
	imgNp = np.array(bytearray(imgResp.read()), dtype=np.uint8)
	
	img = cv2.imdecode(imgNp, -1)
	cv2.imshow('temp',cv2.resize(img,None,fx=0.5, fy=0.5))
	q = cv2.waitKey(1)

cv2.destroyAllWindows()
		   

