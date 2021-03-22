import cv2
lena = cv2.imread("02/lena.bmp")
cv2.imshow("Demo",lena)
key = cv2.waitKey()
if key == ord('A'):
    cv2.imshow("PressA",lena)
elif key == ord('B'):
    cv2.imshow("PressB",lena)
cv2.waitKey()
