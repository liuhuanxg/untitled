"""
对称二叉树（LeetCode 101，简单）
判断二叉树是否镜像对称。
    1
   / \
  2   2
 / \ / \
3  4 4  3   -> True

    1
   / \
  2   2
   \   \
   3    3   -> False

思路提示：递归比较「左子树的左」与「右子树的右」、「左子树的右」与「右子树的左」。
"""


class TreeNode():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_symmetric(root):
    pass


if __name__ == '__main__':
    root = TreeNode(1,
                    TreeNode(2, TreeNode(3), TreeNode(4)),
                    TreeNode(2, TreeNode(4), TreeNode(3)))
    assert is_symmetric(root) is True

    root2 = TreeNode(1,
                     TreeNode(2, None, TreeNode(3)),
                     TreeNode(2, None, TreeNode(3)))
    assert is_symmetric(root2) is False
    print("all tests passed")
