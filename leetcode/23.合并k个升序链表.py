#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File Name: 23.合并k个升序链表.py
Created Time: 2024/8/13 23:13
"""

"""

给你一个链表数组，每个链表都已经按升序排列。

请你将所有链表合并到一个升序链表中，返回合并后的链表。

示例 1：
输入：lists = [[1,4,5],[1,3,4],[2,6]]
输出：[1,1,2,3,4,4,5,6]
解释：链表数组如下：
[
  1->4->5,
  1->3->4,
  2->6
]
将它们合并到一个有序链表中得到。
1->1->2->3->4->4->5->6

示例 2：
输入：lists = []
输出：[]

示例 3：
输入：lists = [[]]
输出：[]
 

提示：

k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] 按 升序 排列
lists[i].length 的总和不超过 10^4
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def mergeTwoLists(self, list1, list2):
        cur = dum = ListNode(0)
        while list1 and list2:
            if list1.val < list2.val:
                cur.next, list1 = list1, list1.next
            else:
                cur.next, list2 = list2, list2.next
            cur = cur.next
        cur.next = list1 if list1 else list2
        return dum.next

    def mergeKLists(self, lists):
        if len(lists) < 1:
            return None
        if len(lists) == 1:
            return lists[0]
        head = lists[0]
        for i in range(1, len(lists)):
            head = self.mergeTwoLists(head, lists[i])
        return head


if __name__ == '__main__':
    s = Solution()
    ret = s.mergeKLists([ListNode(2, ListNode(4)), ListNode(1, ListNode(3)), ListNode(6, ListNode(7))])
    print()
    while ret:
        print(ret.val)
        ret = ret.next
