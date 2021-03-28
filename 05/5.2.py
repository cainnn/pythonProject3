import cv2

img = cv2.imread("test.bmp")
r, c = img.shape[:2]
size = (int(c * 0.9), int(r * 0.5))
rst = cv2.resize(img,size)
print("img.shape=", img.shape)
print("rst.shape=", rst.shape)
cv2.imshow("img",img)
cv2.imshow("rst",rst)
cv2.waitKey()
cv2.destroyAllWindows()