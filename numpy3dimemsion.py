import numpy as np
x = np.arange(27)
# print(x)
x = np.reshape(x,(3,3,3))
# print(x)
# print(x[0])
# print(x[0,1])
# print(x[:,:,0])
print(x[:,0,:])