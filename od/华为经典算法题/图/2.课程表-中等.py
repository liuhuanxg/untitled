"""
课程表（LeetCode 207，中等）— 拓扑排序 / 环检测
numCourses 门课，prerequisites[i] = [a, b] 表示修课程 a 前必须先修课程 b。
判断是否能修完所有课程（即依赖图中不存在环）。
numCourses=2, prerequisites=[[1,0]]          -> True
numCourses=2, prerequisites=[[1,0],[0,1]]   -> False（存在环）
numCourses=3, prerequisites=[[1,0],[2,1]]   -> True

思路提示：
- 建图：b -> a 的有向边，统计每个节点的入度；
- Kahn 算法：把入度为 0 的节点入队，逐层删边、减入度，最后能删完所有节点（拓扑数==课程数）即无环；
- 或用 DFS 三色标记（白/灰/黑）检测回边。
"""


def can_finish(num_courses, prerequisites):
    pass


if __name__ == '__main__':
    assert can_finish(2, [[1, 0]]) is True
    assert can_finish(2, [[1, 0], [0, 1]]) is False
    assert can_finish(3, [[1, 0], [2, 1]]) is True
    assert can_finish(4, [[1, 0], [2, 1], [3, 2]]) is True
    print("all tests passed")
