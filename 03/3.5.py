import cv2
import numpy as np

a = cv2.imread("boat.bmp")
b = cv2.imread("lena512.bmp")
c = cv2.addWeighted(a, 0.3, b, 0.7, 0)
cv2.imshow("boat", a)
cv2.imshow("lena", b)
cv2.imshow("merge", c)
cv2.waitKey()
cv2.destroyAllWindows()
