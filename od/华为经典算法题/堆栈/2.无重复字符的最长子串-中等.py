"""
无重复字符的最长子串（LeetCode 3，中等）— 滑动窗口
输入："abcabcbb" -> 3（"abc"）
输入："bbbbb"    -> 1
输入："pwwkew"   -> 3（"wke" 或 "kew"）
输入：""         -> 0

思路提示：
- 双指针 [left, right] 维护窗口，哈希表记录字符最近出现的位置；
- 右指针前进，若当前字符已在窗口内（位置 >= left），则把 left 跳到该字符上次位置 +1；
- 每步更新最大窗口长度。
"""


def length_of_longest_substring(s):
    pass


if __name__ == '__main__':
    assert length_of_longest_substring("abcabcbb") == 3
    assert length_of_longest_substring("bbbbb") == 1
    assert length_of_longest_substring("pwwkew") == 3
    assert length_of_longest_substring("") == 0
    assert length_of_longest_substring("au") == 2
    print("all tests passed")
