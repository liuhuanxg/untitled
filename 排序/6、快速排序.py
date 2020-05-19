#-*-coding:utf-8 -*-

"""
算法思想：首先找一个基准值，比基准值小的放在左边列表，比基准值大的放在右边列表，再分别在两边的列表中进行重复的操作，直到每个列表的长度<=1

时间复杂度平均为O(nlog2n),最好为O(nlog2n),最坏O(n2)，空间复杂度为O(nlog2n)，不稳定排序

"""


"""
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        base = arr[0]
        less = [v for v in arr[1:] if v<=base]
        more = [v for v in arr[1:] if v>base]
        return quick_sort(less) + [base] + quick_sort(more)
lst = [1, 23, 74, 64, 3, 6, 2, 53, 57, 12]
print(quick_sort(lst))
"""

"""
list1 = [9,6,8,4,7]
for i in range(len(list1)):
    for j in range(len(list1)-1-i):
        if list1[j]<list1[j+1]:
            list1[j],list1[j+1] =list1[j+1], list1[j]
print(list1)
"""

"""
def func(nums, target):
    
    # :param nums: 传入的正序列表
    # :param target: 传入的整数
    # :return:   列表中某两个数的和等于target，就把那两个数的下标返回
    
    nums1 = len(nums)
    a = -1
    for b in range(1, nums1):
        t = nums[b:]
        if (target - nums[b]) in t:
            a = t.index(target - nums[b])
            break
        elif a > 0:
            return [b, a]
"""


"""
def func(nums,target):
    i = 0
    j = len(nums) - 1
    while i<j:
        if nums[i]+nums[j] == target:
            return [i,j]
        elif nums[i]+nums[j] > target:
            j -= 1
            i -= 1
        i += 1
"""