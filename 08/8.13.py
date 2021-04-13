import cv2
o = cv2.imread("kernel.bmp",cv2.IMREAD_UNCHANGED)
k1 = cv2.getStructuringElement(cv2.MORPH_RECT, (59, 59))
k2 = cv2.getStructuringElement(cv2.MORPH_CROSS, (59, 59))
k3 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (59, 59))
dst1 = cv2.dilate(o,k1)
dst2 = cv2.dilate(o,k2)
dst3 = cv2.dilate(o,k3)
cv2.imshow("o", o)
cv2.imshow("dst1", dst1)
cv2.imshow("dst2", dst2)
cv2.imshow("dst3", dst3)
cv2.waitKey()
cv2.destroyAllWindows()