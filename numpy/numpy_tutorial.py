import numpy as np
import time
import sys
SIZE = 1000000
l1 = range(SIZE)
l2 = range(SIZE)

a1 = np.arange(SIZE)
a2 = np.arange(SIZE)

start = time.time()
list_result = [(x+y) for x,y in zip(l1,l2)]
print("python list took :",(time.time()-start) * 1000)
# print(list_result)

np_time = time.time()
numpy_result = a1+a2
print("time of np_result :", (time.time()-np_time) * 1000)
# print(numpy_result)


# Flatten using numpy:
a = np.array([[6,7,8], [1,2,3],[3,4,5]])

for cell in a.flat:
    print("flatten value :",cell)

