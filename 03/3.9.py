import numpy as np
import cv2

a = np.ones((3, 3), dtype=np.uint8)
mask = np.zeros((3, 3), dtype=np.uint8)
mask[1:3, 1:3] = 1
print(mask)
b = cv2.bitwise_and(a, a,mask=mask)
print(b)
