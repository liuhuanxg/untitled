"""
最长回文子串（LeetCode 5，中等）
输入："babad" -> "bab" 或 "aba"
输入："cbbd"  -> "bb"
输入："a"     -> "a"
输入："ac"    -> "a" 或 "c"

思路提示：中心扩展法。
- 每个位置都可作为「奇数长度」中心（单字符）和「偶数长度」中心（两字符之间）；
- 从中心向两侧扩展，记录能扩展到的最长回文。
- 进阶：Manacher 算法可 O(n) 解决。
"""


def longest_palindrome(s):
    pass


if __name__ == '__main__':
    assert longest_palindrome("babad") in ("bab", "aba")
    assert longest_palindrome("cbbd") == "bb"
    assert longest_palindrome("a") == "a"
    assert longest_palindrome("ac") in ("a", "c")
    assert longest_palindrome("") == ""
    print("all tests passed")
