import  cv2
import numpy as np
img = cv2.imread("gradient.bmp",cv2.IMREAD_UNCHANGED)
k = np.ones((5,5),np.uint8)
r = cv2.morphologyEx(img,cv2.MORPH_GRADIENT,k)
cv2.imshow("img",img)
cv2.imshow("r",r)
cv2.waitKey()
cv2.destroyAllWindows()