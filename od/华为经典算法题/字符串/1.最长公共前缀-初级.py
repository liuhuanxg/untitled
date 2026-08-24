"""
最长公共前缀（LeetCode 14，简单）
输入：["flower","flow","flight"] -> "fl"
输入：["dog","racecar","car"]    -> ""
输入：["ab","a"]                 -> "a"

思路提示：
- 纵向扫描：逐列比较所有字符串的第 i 个字符，出现不一致或某串到头即截断。
- 或先排序，只比较首串与尾串的最长公共前缀。
"""


def longest_common_prefix(strs):
    pass


if __name__ == '__main__':
    assert longest_common_prefix(["flower", "flow", "flight"]) == "fl"
    assert longest_common_prefix(["dog", "racecar", "car"]) == ""
    assert longest_common_prefix(["ab", "a"]) == "a"
    assert longest_common_prefix(["single"]) == "single"
    print("all tests passed")
