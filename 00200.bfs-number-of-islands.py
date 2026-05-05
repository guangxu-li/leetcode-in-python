#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# Constraints:
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'.

# @lc code=start
from collections import deque
from typing import List

DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

class Solution:
    # expand expands the island from (i, j) to all directions in a BFS manner.
    def expand(self, grid: List[List[str]], i, j: int) -> None:
        out_of_bound = lambda i, j: i < 0 or i >= self.m or j < 0 or j >= self.n
        q = deque([(i, j)])

        while q:
            x, y = q.popleft()
            if out_of_bound(x, y):
                continue
            if self.grid[x][y] == '0':
                continue
            self.grid[x][y] = '0'

            for dir in DIRS:
                nx, ny = x + dir[0], y + dir[1]
                q.append((nx, ny))

        return

    def numIslands(self, grid: List[List[str]]) -> int:
        self.grid = grid
        self.m = len(grid)
        self.n = len(grid[0])

        cnt = 0
        for i in range(self.m):
            for j in range(self.n):
                cnt += int(self.grid[i][j])
                self.expand(grid, i, j)

        return cnt

# @lc code=end
