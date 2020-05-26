# dict1 = {10:"A",11:"B",12:"C",13:"D",14:"E",}
# def func1(n):
#     str1 = ''
#     while n > 0:
#         m = n - int(n/14)*14
#         if m in dict1:
#             m=dict1[m]
#         n = int(n/14)
#         str1 += str(m)
#         print(str1)
#     print(str1[::-1])
# if __name__ == '__main__':
#     func1(84*148)

# for i in range(4,0,-1):
#     print(i)

#--coding:utf-8
def func(nums,target):
    i = len(nums)-1
    j = 0
    while i>j:
        if nums[i]<target:
            if nums[i]+nums[j] == target:
                return [j,i]
            elif nums[i] + nums[j]<target:
                j += 1
        i -= 1
    return "not find"

if __name__ == '__main__':
    nums = [2, 7, 8, 9]
    print(func(nums,9))