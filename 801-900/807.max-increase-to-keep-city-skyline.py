#
# @lc app=leetcode id=807 lang=python3
#
# [807] Max Increase to Keep City Skyline
#

# @lc code=start
from typing import List


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)

        row_max = [max(row) for row in grid]
        col_max = [max(col) for col in zip(grid)]

        return sum(min(row_max[r], col_max[c]) - grid[r][c] for r in range(n) for c in range(n))


# @lc code=end
