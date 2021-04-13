import cv2
import numpy as np

img1 = cv2.imread("tophat.bmp",cv2.IMREAD_UNCHANGED)
img2 = cv2.imread("lena.bmp",cv2.IMREAD_UNCHANGED)
k = np.ones((5,5),np.uint8)
r1 = cv2.morphologyEx(img1,cv2.MORPH_TOPHAT,k)
r2 = cv2.morphologyEx(img2,cv2.MORPH_TOPHAT,k)
cv2.imshow("img1",img1)
cv2.imshow("r1",r1)
cv2.imshow("img2",img2)
cv2.imshow("r2",r2)
cv2.waitKey()
cv2.destroyAllWindows()