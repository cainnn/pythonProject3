import cv2
import numpy as np
lena = cv2.imread("lenacolor.png")
b,g,r = cv2.split(lena)
cv2.imshow("B",b)
cv2.imshow("G",g)
cv2.imshow("R",r)
cv2.waitKey()
cv2.destroyAllWindows()