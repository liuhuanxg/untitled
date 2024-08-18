#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
给你两个非空 的链表，表示两个非负的整数。它们每位数字都是按照逆序的方式存储的，并且每个节点只能存储一位数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0开头。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/add-two-numbers
输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.

输入：l1 = [0], l2 = [0]
输出：[0]

输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
输出：[8,9,9,9,0,0,0,1]

"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1_queue = [l1.val]
        l2_queue = [l2.val]

        while l1.next:
            l1_queue.insert(0, l1.next.val)
            l1 = l1.next

        while l2.next:
            l2_queue.insert(0, l2.next.val)
            l2 = l2.next

        # print(l1_queue, l2_queue)

        l1_length = len(l1_queue)
        l2_length = len(l2_queue)
        index = -1
        sum_lst = []
        max_length = max(l1_length, l2_length)
        flag = 0
        while index >= -max_length or flag:
            if index >= -l1_length:
                value1 = l1_queue[index]
            else:
                value1 = 0
            if index >= -l2_length:
                value2 = l2_queue[index]
            else:
                value2 = 0
            this_sum = value1 + value2 + flag
            if this_sum >= 10:
                flag = 1
                this_sum -= 10
            else:
                flag = 0
            # print("this_sum:{}, index:{},flag:{},value1:{},value2:{}".format(this_sum, index, flag, value1, value2))
            sum_lst.insert(0, this_sum)
            index -= 1
        first_node = ListNode(sum_lst[0], None)
        node = ListNode(sum_lst[0], None)
        # print(sum_lst)
        if len(sum_lst) > 1:
            for i in sum_lst[1:]:
                node = ListNode(i, None)
                node.next, first_node = first_node, node
        return node


if __name__ == '__main__':
    s = Solution()
    # print(s.addTwoNumbers(
    #     ListNode(2,
    #              ListNode(4,
    #                       ListNode(3, None)
    #                       )
    #              ),
    #     ListNode(5,
    #              ListNode(6,
    #                       ListNode(4, None)
    #                       )
    #              )
    # )
    # )

    print(s.addTwoNumbers(
        ListNode(9,
                 ListNode(9,
                          ListNode(9, ListNode(9, None))
                          )
                 ),
        ListNode(9,
                 ListNode(9,
                          ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, None)))))
                          )
                 )
    )
    )
    """
    [9,9,9,9,9,9,9]
[9,9,9,9]
    """
