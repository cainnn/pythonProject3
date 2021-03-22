import cv2

img = cv2.imread("lenacolor.png", cv2.IMREAD_UNCHANGED)
face = img[220:400, 250:350]
cv2.imshow("original", img)
cv2.imshow("face", face)
cv2.waitKey()
cv2.destroyAllWindows()
