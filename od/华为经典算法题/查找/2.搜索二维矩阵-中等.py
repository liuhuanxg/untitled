"""
搜索二维矩阵（LeetCode 74，中等）
矩阵特征：每行升序，且每行首元素大于上一行尾元素。判断 target 是否存在。
matrix = [[1,3,5,7],
          [10,11,16,20],
          [23,30,34,60]]
target=3  -> True；target=13 -> False

思路提示：把矩阵视作一维升序数组，下标 mid 映射为 matrix[mid//n][mid%n]，直接二分。
"""


def search_matrix(matrix, target):
    pass


if __name__ == '__main__':
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    assert search_matrix(matrix, 3) is True
    assert search_matrix(matrix, 13) is False
    assert search_matrix(matrix, 60) is True
    assert search_matrix([[]], 1) is False
    print("all tests passed")
