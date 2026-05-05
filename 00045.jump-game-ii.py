#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#

# @lc code=start
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        # This is a greedy algorithm.
        # But it can also be understood as an implicit BFS.
        #
        # Try to understand it in this way:
        #  - next_range is the last index to be handled in next level
        #  - when i reaches cur_range, it means we have handled the current level
        #  - the number of levels is the number of jumps
        jumps, cur_range, next_range = 0, 0, 0

        for i, num in enumerate(nums):
            next_range = max(next_range, i + num)
            if i == cur_range:
                jumps += 1
                cur_range = next_range

        return jumps


# @lc code=end
