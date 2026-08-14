"""
题目描述

给定一组推理请求的区间 [start, end]，选出最多的互不重叠区间。

示例：

- 输入 [[1,2],[3,5],[6,7]]，输出 3
- 输入 [[1,3],[2,4],[3,3],[4,4]]，输出 2（选 [1,3] 和 [4,4]）

### 解题思路

**贪心算法**：

- 按区间**结束位置**升序排序
- 优先选结束早的区间，给后续留更多空间
- 遍历时判断当前区间起始位置是否大于上一个选中区间的结束位置

为什么按结束位置排序：结束越早，留给后面的空间越大，能塞进更多不重叠区间。

"""

class Solution:
    def max_llm_batch(self, requests) -> int:
        if not requests:
            return 0

        # 按结束位置升序排序
        requests.sort(key=lambda x: x[1])

        count = 1
        end = requests[0][1]

        for i in range(1, len(requests)):
            if requests[i][0] > end:  # 不重叠
                count += 1
                end = requests[i][1]

        return count

if __name__ == '__main__':

    s = Solution()

    # 用例1：基本用例，不重叠
    assert s.max_llm_batch([[1,2],[3,5],[6,7]]) == 3

    # 用例2：有重叠，需要选择
    assert s.max_llm_batch([[1,3],[2,4],[3,3],[4,4]]) == 2

    # 用例3：完全重叠
    assert s.max_llm_batch([[1,5],[1,5],[1,5]]) == 1

    # 用例4：首尾相连（不算重叠，起始>结束才算不重叠）
    assert s.max_llm_batch([[1,2],[2,3],[3,4]]) == 2  # 如果边界相等算重叠
    # assert s.max_llm_batch([[1,2],[2,3],[3,4]]) == 3  # 如果边界相等不算重叠

    # 用例5：单个区间
    assert s.max_llm_batch([[1,10]]) == 1

    # 用例6：所有区间互不重叠
    assert s.max_llm_batch([[1,2],[4,5],[7,8],[10,11]]) == 4

    # 用例7：嵌套区间
    assert s.max_llm_batch([[1,10],[2,3],[4,5],[6,7]]) == 3

    # 用例8：大量重叠，只能选1个
    assert s.max_llm_batch([[1,100],[2,99],[3,98],[4,97]]) == 1

    # 用例9：空列表
    assert s.max_llm_batch([]) == 0

    # 用例10：长度为1的区间
    assert s.max_llm_batch([[1,1],[2,2],[3,3]]) == 3

    print("全部测试通过 ✅")