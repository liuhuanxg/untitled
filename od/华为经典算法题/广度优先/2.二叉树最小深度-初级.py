"""
二叉树的最小深度（LeetCode 111，简单）— BFS 层序遍历
从根节点到最近叶子节点的最短路径上的节点数（必须到叶子节点，不能遇空即返）。
输入：[3,9,20,null,null,15,7] -> 2
输入：[2,null,3,null,4,null,5,null,6] -> 5

思路提示：BFS 首次遇到叶子节点即可返回当前层数，无需遍历整棵树。
"""


class TreeNode():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def min_depth(root):
    pass


if __name__ == '__main__':
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert min_depth(root) == 2

    root2 = TreeNode(2, None,
                     TreeNode(3, None,
                              TreeNode(4, None,
                                       TreeNode(5, None, TreeNode(6)))))
    assert min_depth(root2) == 5
    print("all tests passed")
