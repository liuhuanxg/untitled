import numpy as np
arr=np.arange(20).reshape(4,5)
print(arr)
print('总和：',np.sum(arr))
print('所有元素和：',np.cumsum(arr))