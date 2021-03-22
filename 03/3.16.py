import cv2
import numpy as np

lena = cv2.imread("lena512.bmp", 0)
r, c = lena.shape
mask = np.zeros((r, c), dtype=np.uint8)
mask[220:400, 250:350] = 1
key = np.random.randint(0, 256, size=[r, c], dtype=np.uint8)
# ========获取打码脸===========
# 使用密钥key对原始图像lena加密
lenaXorKey = cv2.bitwise_xor(lena, key)
# 获取加密图像的脸部信息encryptFace
encryptFace = cv2.bitwise_and(lenaXorKey, mask * 255)
# 将图像lena内的脸部值设置为0，得到noface1
noFace1 = cv2.bitwise_and(lena, (1 - mask) * 255)
# 得到打码的lena图像
maskFace = encryptFace + noFace1
# ========将打码脸解码==========
# 将脸部打码的lena与密钥key进行异或运算，得到脸部的原始信息
extractOriginal = cv2.bitwise_xor(maskFace, key)
# 将解码的脸部信息extractOriginal提取出来，得到extractFace
extractFace = cv2.bitwise_and(extractOriginal, mask * 255)
# 从脸部打码的lena内提取没有脸部信息的lena图像，得到 noface2
noFace2 = cv2.bitwise_and(maskFace, (1 - mask) * 255)
# 得到解码的lena图像
extractLena = noFace2 + extractFace
# ===========显示图像============
cv2.imshow("lena", lena)
cv2.imshow("mask", mask * 255)
cv2.imshow("1-mask", (1 - mask) * 255)
cv2.imshow("key", key)
cv2.imshow("lenaXorKey", lenaXorKey)
cv2.imshow("encryptFAce", encryptFace)
cv2.imshow("noFAce1", noFace1)
cv2.imshow("maskFAce", maskFace)
cv2.imshow("extractOriginal", extractOriginal)
cv2.imshow("extractFAce", extractFace)
cv2.imshow("noFAce2", noFace2)
cv2.imshow("extractLena", extractLena)
cv2.waitKey()
cv2.destroyAllWindows()
