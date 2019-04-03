#分治：分而治之
#使用分治法能解决的问题一般具有以下几个特征：

'''
（1）、该问题的规模缩小到一定程度就可以相对容易的解决
（2）、该问题可以分解为若干个规模较小的相同问题，即该问题具有最优子结构性质
（3）、利用该问题分解出的子问题的解可以合并为该问题的解
（4）、该问题所分解出的各个子问题是相互独立的，即子问题之间不包含公共的子问题
'''
#例题：给定一个顺序表，编写一个求出其最大值的分治算法

import time


#基本子算法（子问题规模小于等于2时）
def get_max(nums):
    if len(nums)<2:
        return nums[0]
    if nums[0]<nums[1]:
        return nums[1]
    else:
        return nums[0]

def solve(init_list):
    n=len(init_list)
    if n<=2:  #若问题规模小于等于2，直接解决（不用再分治）
        return get_max(init_list)

    #分解（子问题规模为2--即两两比较，如果是奇数项，最后一个列表的规模为1）
    temp_list=(init_list[i:i+2] for i in range(0,n,2))

    #分治  合并
    list=[]
    for new_list in temp_list:
        list.append(get_max(new_list))

    return solve(list)

if __name__ == '__main__':
    init_list = [x for x in range(10**7)]
    start_time=time.time()
    max=solve(init_list)
    print('最大值为：',max)
    end_time=time.time()
    print(end_time-start_time)
#5.987342596054077


'''
init_list = [x for x in range(10**4)]
start_time=time.time()
for x in init_list:
    for i in range(len(init_list)-1):
        if init_list[i]<init_list[i+1]:
            init_list[i],init_list[i+1]=init_list[i+1],init_list[i]
print(init_list[0])
end_time=time.time()
print(end_time-start_time)
#27.812590837478638
'''

# ary=[4,3,6,2,7,8,1]
# j=1
# while j<len(ary):
#     for i in range(len(ary)-j):
#         if ary[i]>ary[i+1]:
#              ary[i],ary[i+1]=ary[i+1],ary[i]
#     j+=1
# print(ary)
