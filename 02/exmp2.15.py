import cv2
lena = cv2.imread("lena512.bmp", cv2.IMREAD_UNCHANGED)
dolloar = cv2.imread("../dollar.bmp", cv2.IMREAD_UNCHANGED)
cv2.imshow("lena",lena)
cv2.imshow("dollar",dolloar)
face = lena[220:400,250:350]
dolloar[160:340,200:300] = face
cv2.imshow("result",dolloar)
cv2.waitKey()
cv2.destroyAllWindows()