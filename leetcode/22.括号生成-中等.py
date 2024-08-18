#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File Name: 22括号生成.py

给出n代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合
例如：
    输入 1 ()
    输入 2 (()), ()()
    输入 3 ((())),(())(),()(()), ()()(),
    输入 4 (((()))), ((()))(), (())(()), ()((()))

方法：
    1. 把所有的结果用数学归纳法计算
    2. Recursion，使用递归，拆分为2n个字符串，遍历所有的可能性，时间复杂度2的2n次方
    3. 改进，时间复杂度2的n次方：
        1. 局部不合法，不在递归
        2. left used，right used
"""


class Solution():

    def generateParenthesis(self, n):
        self.result = []
        self._gen(0, 0, n, "")
        return self.result

    def _gen(self, left, right, n, result):
        """
        left 表示左括号已经用的个数
        right 表示右括号已经用的个数
        n 表示括号个数
        result 表示最终的返回结果
        """
        if left == right == n:
            self.result.append(result)
            return
        """
        n = 2
        gen(0,0,n,"")  
            gen(1, 0, n, ( )
                gen(2, 0, n ,(( )
                    gen(2, 1, n ,(() )
                    gen(2, 2, n ,(()) )
                gen(1, 1, n ,())
                    gen(2, 1, n ,()()
                    gen(2, 2, n ,()())
        
        left:1, right:0, result:(
        left:2, right:0, result:((
        left:2, right:1, result:(()
        left:2, right:2, result:(())
        left:1, right:1, result:()
        left:2, right:1, result:()(
        left:2, right:2, result:()()
        
        """
        if left < n:
            self._gen(left + 1, right, n, result + "(")
        if left > right and right < n:
            self._gen(left, right + 1, n, result + ")")


if __name__ == '__main__':
    s = Solution()
    print(s.generateParenthesis(2))
    # print(s.generateParenthesis(3))
    # print(s.generateParenthesis(4))
