import cv2
import numpy as np
img = np.zeros((5,5),np.uint8)
# img = np.arange(25).reshape(5,5)

# arr = np.arange(1,26).reshape(5,5)
# print(arr)
# print(img)
# img = np.reshape(img,(5,5))
# print(img)
img[1:4,1:4] = 1
kernel = np.ones((3,1),np.uint8)
erosion = cv2.erode(img,kernel)
print("img=\n",img)
print("kernel=\n",kernel)
print("erosion=\n",erosion)
