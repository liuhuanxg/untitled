"""
反转单链表（LeetCode 206，简单）
输入：1 -> 2 -> 3 -> 4 -> 5 -> NULL
输出：5 -> 4 -> 3 -> 2 -> 1 -> NULL

思路提示：
- 迭代法：三指针（prev/cur/nxt），边遍历边把 cur.next 指向 prev；
- 递归法：先递归到尾节点，回溯时把后一个节点指向自己，自己 next 置空。
"""


class ListNode():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

"""
1 -> 2 -> 3 -> 4 -> 5
cur 1 
prev 1 
head 1

cur 2
next = cur.next
cur.next = ListNode(prev.val)
prev = next
"""


def reverse_list(head):
    prev = None  # 已反转部分的头（初始为空）
    cur = head  # 当前待处理的节点
    while cur:
        nxt = cur.next  # 1. 先记下下一个节点，否则待会会丢失
        cur.next = prev  # 2. 把当前节点的箭头反向，指向前一个
        prev = cur  # 3. prev 前移到当前节点
        cur = nxt  # 4. cur 前移到刚才记下的下一个节点
    return prev  # 循环结束 cur 为 None，prev 就是新头


def reverse_list_recursive(head):
    # 基线条件：空链表，或到达尾节点（next 为空）
    if not head or not head.next:
        return head

    # 先递归到尾，new_head 就是原链表的最后一个节点（新头）
    new_head = reverse_list_recursive(head.next)

    # 回溯：让后一个节点指向当前节点（反向箭头）
    head.next.next = head
    # 断开当前节点原来的指向，避免成环
    head.next = None

    return new_head


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
    h = build([1, 2, 3, 4, 5])
    assert to_list(reverse_list(h)) == [5, 4, 3, 2, 1]
    # h = build([1, 2, 3, 4, 5])
    # assert to_list(reverse_list_recursive(h)) == [5, 4, 3, 2, 1]
    # assert to_list(reverse_list(build([]))) == []
    # print("all tests passed")
