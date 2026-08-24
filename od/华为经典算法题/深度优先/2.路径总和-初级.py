"""
路径总和（LeetCode 112，简单）— DFS
判断是否存在一条从根到叶子节点的路径，其节点值之和等于 targetSum。
       5
      / \
     4   8
    /   / \
   11  13  4
  /  \      \
 7    2      1
targetSum=22 -> True（路径 5->4->11->2 = 22）
targetSum=27 -> False

思路提示：DFS 递归，每下一层把 targetSum 减去当前节点值，到叶子时判断剩余是否为 0。
"""


class TreeNode():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def has_path_sum(root, target_sum):
    pass


if __name__ == '__main__':
    n7 = TreeNode(7); n2 = TreeNode(2)
    n11 = TreeNode(11, n7, n2)
    n4 = TreeNode(4, n11, None)
    n13 = TreeNode(13); n1 = TreeNode(1)
    n8 = TreeNode(8, n13, TreeNode(4, None, n1))
    root = TreeNode(5, n4, n8)

    assert has_path_sum(root, 22) is True
    assert has_path_sum(root, 27) is False
    print("all tests passed")
