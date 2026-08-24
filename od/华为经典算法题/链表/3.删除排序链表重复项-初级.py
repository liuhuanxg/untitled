"""
删除排序链表中的重复元素（LeetCode 83，简单）
给定升序链表，使每个元素只出现一次。
输入：1 -> 1 -> 2        -> 1 -> 2
输入：1 -> 1 -> 2 -> 3 -> 3 -> 1 -> 2 -> 3

思路提示：题目保证输入有序，重复必相邻。单指针一次遍历，遇 cur.val == cur.next.val 则跳过 next。
"""


class ListNode():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def delete_duplicates(head):
    dumpy = head
    while head and head.next:
        if head.val == head.next.val:
            head.next = head.next.next
        else:
            head = head.next
    return dumpy



def build(arr):
    dummy = ListNode()
    cur = dummy
    for v in arr:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


def to_list(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res


if __name__ == '__main__':
    assert to_list(delete_duplicates(build([1, 1, 2]))) == [1, 2]
    assert to_list(delete_duplicates(build([1, 1, 2, 3, 3]))) == [1, 2, 3]
    assert to_list(delete_duplicates(build([1, 1, 1]))) == [1]
    print("all tests passed")
