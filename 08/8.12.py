import cv2

k1 = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
k2 = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))
k3 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
print("k1=\n",k1)
print("k2=\n",k2)
print("k3=\n",k3)