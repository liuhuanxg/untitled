import numpy as np
'''
1、使用array函数来创建
格式： np.array(object,dtype=None,copy=True,oreder='K',subok=False,ndmin=0)
objece：接受array。表示想要创建的数据，无默认值
dtype: 接受data-type.表示数组所需的数据类型。如果未给定，则选择保存对象所需的最小类型。默认为None
ndmin:接收int。指定生成数据应该具有的最小维数，默认为None
'''
a1=np.array([1,2,3,4])
print(a1,a1.dtype)     #[1 2 3 4] int32
a2=np.array([1,2,3.14,4])
print(a2,a2.dtype)    #[1.   2.   3.14 4.  ] float64
a2=np.array([1,2,3.14,4],dtype=int)
print(a2,a2.dtype)    #[1 2 3 4] int32

a4=np.array([(1,2),(3,4)])
print(a4,a4.ndim)
'''
[[1 2]
 [3 4]] 2'''
a5=np.array([[1,2],[3,4]])
print(a5,a5.ndim)
'''
[[1 2]
 [3 4]] 2'''

#2、arange()
#格式：arange(开始值，终止值，步长)  [开始值，终止值]
arr6=np.arange(1,9,1)
print(arr6)

arr7=np.arange(0,1,0.22)
print(arr7)  #缺点是元素个数预估有难度


#3、linspace
#格式：linspace(开始值，终止值，元素个数)
arr8=np.linspace(0.1,1,7)   #float型
print(arr8)    #[ 0.1   0.25  0.4   0.55  0.7   0.85  1.  ]


#使用logspace()函数
#生成10~1 到10~3之间的等比例数
arr9=np.logspace(1,3,3)    #float型
print('arr9',arr9)

#其他函数
a12=np.zeros((2,3))  #生成2行3列的0
print(a12)

#empty()函数
a13=np.empty((2,3))
print(a13)

#eye(N)函数
#生成N阶矩阵，并且对角线元素为1
a14=np.eye(3)
print(a14)

#使用diag()函数
a15=np.diag([1,2,3,4])   #对角线为1,2,3,4.其他为0
print(a15)