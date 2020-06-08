#-*-coding:utf-8 -*-
"""
@project:untitled
@File: 12、翻转链表.py
@Time: 2020/6/1 13:57
@user：liuhuan   
"""


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


def rev(link):
    pre = link
    cur = link.next
    pre.next = None
    while cur:
        temp = cur.next
        cur.next = pre
        pre = cur
        cur = temp
    return pre


if __name__ == '__main__':
    link = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8,Node(9)))))))))
    root = rev(link)
    while root:
        print(root.data)
        root = root.next