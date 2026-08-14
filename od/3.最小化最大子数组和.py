"""
题目三：末世资源分配（最小化最大子数组和）

### 题目描述

将数组 nums 分成 k 段连续子数组，使得最大段的和尽量小。

示例：

- 输入 [4,3,6,9,7], k=2
- 输出 16（分成 [4,3,6] 和 [9,7]，最大段和 = 16）

### 解题思路

**二分答案 + 贪心验证**：

核心思路：

1. 答案的范围在 [max(nums), sum(nums)] 之间
  - 下界 max(nums)：每段至少要能放下最大的单个元素
  - 上界 sum(nums)：所有元素放一段
2. 二分猜一个"最大段和" mid
3. 贪心验证：每段不超过 mid，从左到右尽量多装，看需要几段
  - 需要 ≤ k 段 → mid 可行，尝试更小的值
  - 需要 > k 段 → mid 不够，需要更大的值

二分过程示例 [4,3,6,9,7], k=2：

二分范围：[9, 29]

mid=19: [4,3,6](13) [9,7](16) → 2组 ≤ 2 ✅ → right=19
mid=14: [4,3,6](13) [9](9) [7](7) → 3组 > 2 ❌ → left=15
mid=17: [4,3,6](13) [9,7](16) → 2组 ≤ 2 ✅ → right=17
mid=16: [4,3,6](13) [9,7](16) → 2组 ≤ 2 ✅ → right=16
mid=15: [4,3](7) [6,9](15) [7](7) → 3组 > 2 ❌ → left=16

left == right == 16 → 答案 16 ✅
"""
class Solution:
    def alloc(self, nums, k: int) -> int:
        left = max(nums)
        right = sum(nums)

        while left < right:
            mid = (left + right) // 2

            if self.can_split(nums, k, mid):
                right = mid
            else:
                left = mid + 1

        return left

    def can_split(self, nums, k: int, max_sum: int) -> bool:
        groups = 1
        current_sum = 0

        for num in nums:
            if current_sum + num > max_sum:
                groups += 1
                current_sum = num
                if groups > k:
                    return False
            else:
                current_sum += num

        return True