"""
二叉树的右视图（LeetCode 199，中等）— BFS 层序遍历
按层遍历二叉树，取每一层最后一个被访问的节点。
输入：[1,2,3,null,5,null,4]
     1
    / \
   2   3
    \   \
     5   4
输出：[1, 3, 4]

思路提示：队列层序遍历，每层遍历到最后一个节点时记录其值。
"""


class TreeNode():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def right_side_view(root):
    pass


if __name__ == '__main__':
    root = TreeNode(1,
                    TreeNode(2, None, TreeNode(5)),
                    TreeNode(3, None, TreeNode(4)))
    assert right_side_view(root) == [1, 3, 4]
    print("all tests passed")
