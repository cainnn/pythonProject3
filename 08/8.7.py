import cv2
import numpy as np
img1 = cv2.imread("opening.bmp")
img2 = cv2.imread("opening2.bmp")
k = np.ones((10,10),np.uint8)
r1 = cv2.morphologyEx(img1,cv2.MORPH_OPEN,k)
r2 = cv2.morphologyEx(img1,cv2.MORPH_OPEN,k)