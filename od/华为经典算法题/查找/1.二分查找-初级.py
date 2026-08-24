"""
二分查找（LeetCode 704，简单）
在升序数组中查找 target，返回下标；不存在返回 -1。
输入：nums=[-1,0,3,5,9,12], target=9  -> 4
输入：nums=[-1,0,3,5,9,12], target=2  -> -1

思路提示：循环条件用 left <= right，mid = (left+right)//2；根据 nums[mid] 与 target 大小移动 left/right。
"""


def binary_search(nums, target):
    start = 0
    end = len(nums)
    if end == 0:
        return -1
    while start <= end:
        mid = (start + end) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
        print(start, end, mid)
    return -1


if __name__ == '__main__':
    print(binary_search([-1, 0, 3, 5, 9, 12], 9))
    assert binary_search([-1, 0, 3, 5, 9, 12], 9) == 4
    assert binary_search([-1, 0, 3, 5, 9, 12], 2) == -1
    assert binary_search([5], 5) == 0
    assert binary_search([], 1) == -1
    print("all tests passed")
