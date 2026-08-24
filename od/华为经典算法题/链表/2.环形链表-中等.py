"""
环形链表（LeetCode 141/142，简单~中等）
判断链表是否有环；若有则返回入环节点。
输入：head=[3,2,0,-4]，尾节点指向第 2 个节点(值2) -> 有环，入口值为 2

思路提示：快慢指针（Floyd 判圈）。
1) 快指针走 2 步、慢指针走 1 步，相遇说明有环；
2) 相遇后慢指针回到头，两指针同速各走 1 步，再次相遇点即入环节点。
"""


class ListNode():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def detect_cycle(head):
    pass


if __name__ == '__main__':
    n3 = ListNode(3); n2 = ListNode(2); n0 = ListNode(0); n4 = ListNode(-4)
    n3.next = n2; n2.next = n0; n0.next = n4; n4.next = n2
    assert detect_cycle(n3).val == 2

    a = ListNode(1); b = ListNode(2)
    a.next = b
    assert detect_cycle(a) is None
    print("all tests passed")
