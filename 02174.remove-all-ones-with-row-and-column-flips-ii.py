#
# @lc app=leetcode id=2174 lang=python3
#
# [2174] Remove All Ones With Row and Column Flips II
#

# @lc code=start
from typing import List


class Solution:
    def removeOnes(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.zero_rows = set()
        self.zero_cols = set()

        self.m = len(grid)
        self.n = len(grid[0])

        return self.dfs()

    def zero(self, i, j: int) -> None:
        self.zero_rows.add(i)
        self.zero_cols.add(j)

    def revert(self, i, j: int) -> None:
        self.zero_rows.discard(i)
        self.zero_cols.discard(j)

    def dfs(self) -> int:
        res = float("inf")

        for i in range(self.m):
            for j in range(self.n):
                if self.is_zero(i, j):
                    continue

                self.zero(i, j)
                res = min(res, self.dfs() + 1)
                self.revert(i, j)

        return int(res) if res != float("inf") else 0

    def is_zero(self, i, j: int) -> bool:
        return self.grid[i][j] == 0 or i in self.zero_rows or j in self.zero_cols


# @lc code=end
