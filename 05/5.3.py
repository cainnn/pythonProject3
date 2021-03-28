import cv2
img = cv2.imread("test.bmp")
rst = cv2.resize(img,None,fx=2,fy=0.5)
print("img.shape = \n",img.shape)
print("rst.shape = \n",rst.shape)