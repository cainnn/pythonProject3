import cv2
o = cv2.imread("image/bilTest.bmp")
g = cv2.GaussianBlur(o,(55,55),0,0)
b = cv2.bilateralFilter(o,55,200,200)
cv2.imshow("o",o)
cv2.imshow("g",g)
cv2.imshow("b",b)
cv2.waitKey()
cv2.destroyAllWindows()