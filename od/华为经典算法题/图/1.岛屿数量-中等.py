"""
岛屿数量（LeetCode 200，中等）— DFS / BFS / 并查集
grid 中 1 为陆地、0 为水，上下左右相连的陆地算同一个岛，返回岛屿总数。
grid = [[1,1,0,0,0],
        [1,1,0,0,0],
        [0,0,1,0,0],
        [0,0,0,1,1]] -> 3

思路提示：
- 遍历每个格子，遇到 1 时岛屿数 +1；
- 用 DFS 或 BFS 把与它相连的整片陆地标记已访问（置 0 即可）；
- 遍历结束统计到的次数即为岛屿数。O(m*n)。
"""


def num_islands(grid):
    pass


if __name__ == '__main__':
    grid1 = [[1, 1, 0, 0, 0],
             [1, 1, 0, 0, 0],
             [0, 0, 1, 0, 0],
             [0, 0, 0, 1, 1]]
    assert num_islands(grid1) == 3

    grid2 = [[0, 0, 0],
             [0, 0, 0]]
    assert num_islands(grid2) == 0

    grid3 = [[1]]
    assert num_islands(grid3) == 1
    print("all tests passed")
