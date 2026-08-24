"""
翻转二叉树 / 镜像二叉树（LeetCode 226，简单）
每个节点的左右子树互换。
    4             4
   / \           / \
  2   7   ->    7   2
 / \ / \       / \ / \
1  3 6  9     9  6 3  1

思路提示：前序/后序递归（先换子节点再递归，或先递归再换），也可层序迭代。
"""


class TreeNode():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invert_tree(root):
    pass


def preorder(root):
    if not root:
        return []
    return [root.val] + preorder(root.left) + preorder(root.right)


if __name__ == '__main__':
    root = TreeNode(4,
                    TreeNode(2, TreeNode(1), TreeNode(3)),
                    TreeNode(7, TreeNode(6), TreeNode(9)))
    assert preorder(root) == [4, 2, 1, 3, 7, 6, 9]
    assert preorder(invert_tree(root)) == [4, 7, 9, 6, 2, 3, 1]
    print("all tests passed")
