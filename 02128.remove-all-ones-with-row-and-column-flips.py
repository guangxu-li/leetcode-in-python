#
# @lc app=leetcode id=2128 lang=python3
#
# [2128] Remove All Ones With Row and Column Flips
#

# @lc code=start
from typing import List


class Solution:
    def removeOnes(self, grid: List[List[int]]) -> bool:
        target = grid[0]
        # can't use the ~x here due to two's complement
        target_rev = [1 - x for x in grid[0]]

        return all([row == target or row == target_rev for row in grid[1:]])


# @lc code=end
