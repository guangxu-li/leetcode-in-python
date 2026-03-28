#
# @lc app=leetcode id=463 lang=python3
#
# [463] Island Perimeter
#

# @lc code=start
import operator


class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        return sum(
            sum(map(operator.ne, [0] + p, p + [0]))
            for p in grid + [list(r) for r in zip(*grid)]
        )


# @lc code=end
