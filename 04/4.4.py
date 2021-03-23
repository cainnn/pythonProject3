import cv2

lena = cv2.imread("lenacolor.png")
gray = cv2.cvtColor(lena, cv2.COLOR_BGR2GRAY)
rgb = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
print("lena.shape=", lena.shape)
print("gray.shape=", gray.shape)
print("rgb.shape=", rgb.shape)
cv2.imshow("lena", lena)
cv2.imshow("gray", gray)
cv2.imshow("rgb", rgb)
cv2.waitKey()
cv2.destroyAllWindows()
