#
# @lc app=leetcode id=695 lang=python3
#
# [695] Max Area of Island
#

# @lc code=start
from typing import List


class Solution:
    # 1 0
    # 0 1
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        visited = set()
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        valid = lambda x, y: 0 <= x < m and 0 <= y < n and (x, y) not in visited and grid[x][y]

        def areas(i: int, j: int) -> int:
            if not valid(i, j):
                return 0

            visited.add((i, j))

            s = 1
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                s += areas(ni, nj)

            return s

        _max = 0

        for i in range(m):
            for j in range(n):
                _max = max(_max, areas(i, j))

        return _max


# @lc code=end
