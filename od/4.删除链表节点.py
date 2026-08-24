"""
只用一次循环，删除链表中n的节点
例如
1->2->3->4->5->6->7->8->9->10
删除第5个节点
1->2->3->4->6->7->8->9->10

1->2->3->4->5
删除第3个节点
1->2->4->5
start:
    fast = 3
    slow = 1
end:
    fast = 5
    slow = 3
"""
class ListNode():
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def delete_nth(head, n):
    """删除第 n 个节点（从 1 开始计数），只遍历一次"""
    dummy = ListNode(0, next=head)
    prev = dummy
    # 单次循环：移动 n-1 步，停在待删节点的前驱
    for _ in range(n - 1):
        prev = prev.next
    # 跳过第 n 个节点
    prev.next = prev.next.next
    return dummy.next

# 删除倒数第n个节点
def delete_nth_from_end(head, n):
    dummy = ListNode(0, next=head)
    fast = slow = dummy
    for _ in range(n):  # 快指针先走 n 步
        fast = fast.next
    while fast.next:  # 快慢同速，直到快指针到最后一个节点
        print(fast.val, slow.val)
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next  # 删除倒数第 n 个
    return dummy.next

def main():
    head  = delete_nth(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8,
                                                                                                            ListNode(9,
                                                                                                                     ListNode(
                                                                                                                         10))))))))),
                        ),5)
    while head:
        print(head.val)
        head = head.next

if __name__ == '__main__':
    main()