"""
有效的括号（LeetCode 20，简单）— 栈
输入："()"      -> True
输入："()[]{}"  -> True
输入："(]"      -> False
输入："([)]"    -> False
输入："{[]}"    -> True

思路提示：
- 维护一个栈，遇左括号入栈；
- 遇右括号时，若栈为空或栈顶不是对应的左括号，则非法；
- 遍历结束后栈必须为空才合法。
- 注意先判断长度奇偶可提前剪枝。
"""


def is_valid(s):
    pass


if __name__ == '__main__':
    assert is_valid("()") is True
    assert is_valid("()[]{}") is True
    assert is_valid("(]") is False
    assert is_valid("([)]") is False
    assert is_valid("{[]}") is True
    assert is_valid("(((") is False
    print("all tests passed")
