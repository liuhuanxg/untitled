#-*-coding:utf-8 -*-

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
"""
def func(nums,target):
    nums = list(nums)
    for x in range(len(nums)):
        for y in range(x+1,len(nums)):
            print(nums[x],nums[y])
            if nums[x] + nums[y] == target:
                return [x,y]
"""
"""
def func(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] + nums[j] == target and i != j:
                return list([i, j])
"""

# if __name__ == '__main__':
#     nums = [2,7,11,15]
#     target = 18
#     r = func(nums,target)
#     print(r)

list1 = [
    {"name":"zhangsan","age":16},
    {"name":"lisi","age":18},
    {"name":"wangwu","age":19},
    {"name":"zhaoliu","age":20},
    ]
list4 = sorted(list1,key=lambda x:x["age"],reverse=True)
print(list4)

list2 = [2,-4,6]
# list3 = sorted(list2,key=abs,reverse=True)
list2.sort(key=abs,reverse=True)
print(list2)

# def func(nums,target):
#     i = len(nums)-1
#     j = 0
#     while i>j:
#         if nums[i]<target:
#             if nums[i]+nums[j] == target:
#                 return [j,i]
#             elif nums[i] + nums[j]<target:
#                 j += 1
#                 i += 1
#         i -= 1
#     return "not find"

def func(nums,target):
    num1 = nums.copy()
    num1.sort()
    i = 0
    j = 0
    for a in range(0,len(nums)-1):
        if nums[a]+nums[a+1] >= target:
            i = a
            j = a+1
            print(i,j)
            break

if __name__ == '__main__':
    nums = [2, 7, 8, 9]
    print(func(nums,17))

