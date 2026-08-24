"""
前 K 个高频元素（LeetCode 347，中等）— 堆
返回出现频率最高的 k 个元素（顺序不限）。
输入：nums=[1,1,1,2,2,3], k=2 -> [1,2]
输入：nums=[1], k=1            -> [1]

思路提示：
- 用 Counter 统计频率；
- 维护一个大小为 k 的「小顶堆」，堆中始终保留频率最高的 k 个，O(n log k)；
- 也可用快速选择（快排 partition 思想）达到平均 O(n)。
"""
import heapq


def top_k_frequent(nums, k):
    pass


if __name__ == '__main__':
    assert sorted(top_k_frequent([1, 1, 1, 2, 2, 3], 2)) == [1, 2]
    assert top_k_frequent([1], 1) == [1]
    assert sorted(top_k_frequent([4, 1, 4, 1, 4, 2, 2, 3], 2)) == [1, 4]
    print("all tests passed")
