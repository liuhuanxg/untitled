"""
二叉树的最近公共祖先 LCA（LeetCode 236，中等）— DFS
给定二叉树与两个节点 p、q，返回它们的最近公共祖先（节点本身也算自己的祖先）。
       3
     /   \
    5     1
   / \   / \
  6   2 0   8
     / \
    7   4
p=5, q=1 -> 3
p=5, q=4 -> 5

思路提示：后序递归。若当前节点为空或等于 p/q，返回自身；左右子树递归结果若都非空则当前即 LCA；否则返回非空的那个。
"""


class TreeNode():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def lowest_common_ancestor(root, p, q):
    pass


if __name__ == '__main__':
    n7 = TreeNode(7); n4 = TreeNode(4)
    n2 = TreeNode(2, n7, n4)
    n6 = TreeNode(6); n5 = TreeNode(5, n6, n2)
    n0 = TreeNode(0); n8 = TreeNode(8)
    n1 = TreeNode(1, n0, n8)
    root = TreeNode(3, n5, n1)

    assert lowest_common_ancestor(root, n5, n1).val == 3
    assert lowest_common_ancestor(root, n5, n4).val == 5
    print("all tests passed")
