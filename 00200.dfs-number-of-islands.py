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
from typing import List


class Solution:
    def __init__(self) -> None:
        self.grid = None
        self.m = None
        self.n = None

    # expand expands the island from (i, j) to all directions in a DFS manner.
    def expand(self, grid: List[List[str]], i, j: int) -> None:
        out_of_bound = lambda i, j: i < 0 or i >= self.m or j < 0 or j >= self.n
        if out_of_bound(i, j):
            return

        if self.grid[i][j] == '0':
            return

        self.grid[i][j] = '0'
        self.expand(grid, i - 1, j)
        self.expand(grid, i, j + 1)
        self.expand(grid, i + 1, j)
        self.expand(grid, i, j - 1)

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
