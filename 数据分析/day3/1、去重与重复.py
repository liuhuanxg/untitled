import numpy as np

arr=np.arange(5)
print('arr',arr)
new_arr=np.tile(arr,2)
print('new_arr',new_arr)
arr2=new_arr.reshape(2,5)
print('arr2',arr2)

arr3=np.repeat([[1],[2],[3]],2,axis=1)
print('arr3',arr3)

arr4=np.random.randint(0,10,size=(3,3))
print('arr4',arr4)
'''
[[2 6 8]
 [7 4 4]
 [6 2 0]]
 '''
print(arr4.repeat(2,axis=0))
'''
[[2 6 8]
 [2 6 8]
 [7 4 4]
 [7 4 4]
 [6 2 0]
 [6 2 0]]
 '''
print(arr4.repeat(2,axis=1))
'''
[[6 6 4 4 5 5]
 [0 0 7 7 8 8]
 [4 4 0 0 4 4]]
 '''