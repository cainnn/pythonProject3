import cv2
import numpy as np
opencv = cv2.imread("opencv.jpg")
hsv = cv2.cvtColor(opencv,cv2.COLOR_BGR2HSV)
cv2.imshow("opencv", opencv)
# 处理蓝色
minBlue = np.array([110,50,50])
maxBlue = np.array([130,255,255])
mask = cv2.inRange(hsv,minBlue,maxBlue)
blue = cv2.bitwise_and(opencv,opencv,mask=mask)
cv2.imshow("blue",blue)
# 处理绿色
minGreen = np.array([50,50,50])
maxGreen = np.array([70,255,255])
mask = cv2.inRange(hsv,minGreen,maxGreen)
green = cv2.bitwise_and(opencv,opencv,mask=mask)
cv2.imshow("green",green)
# 处理红色
minRed = np.array([0,50,50])
maxRed = np.array([30,255,255])
mask = cv2.inRange(hsv,minRed,maxRed)
red = cv2.bitwise_and(opencv,opencv,mask=mask)
cv2.imshow("red",red)
cv2.waitKey()
cv2.destroyAllWindows()
