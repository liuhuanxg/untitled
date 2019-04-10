import numpy as np
def river(array):
    shape=array.shape
    width=shape[0]-1
    height=shape[1]-1
    sum=0
# [1,2]
# [2,1]
sum=0
flag=True
# 如图所示，有一个 N 行 M 列的棋盘格，有个国际象棋里的马要从这个棋盘格的第一行 跳到最后一行。要求这匹马只能从上往下跳，不能倒着跳，即只能跳往下一行或者下 面第二行。 每个格子上有一个数字，请为小马寻找一条路径，要求路径上所有数之和最小。 小马可以从第一行的任意某个格子开始，也必须到最后一 行 的某个格子结束。 输入：一个 NxM 的矩阵 输出：一个数字，这条路径上所有数之和。
# 附加题（文字阐述你的思路即可，无需代码）： 如果允许小马往回跳，算法有什么不同？



if __name__ == '__main__':
    i = eval(input("输入一个数组："))
    array=np.array(i)
    river(array)
    print(type(array),array)
    print(array[1][1])
    #[[1,2,3,4],[4,5,6,7],[7,8,9,10]]