import cv2
lena = cv2.imread("lena.bmp")
cv2.imshow("before",lena)
for i in range(10,100):
    for j in range(10,100):
        lena[i,j] = 255
cv2.imshow("after",lena)
cv2.waitKey()
cv2.destroyAllWindows()
