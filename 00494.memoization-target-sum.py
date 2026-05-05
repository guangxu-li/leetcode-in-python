#
# @lc app=leetcode id=494 lang=python3
#
# [494] Target Sum
#

# @lc code=start
from typing import Tuple, List
from functools import lru_cache


class Solution:
    @lru_cache(maxsize=20 * 2001)
    def findWays(self, nums: Tuple, pos: int, cur: int) -> int:
        return (
            not cur
            if pos == len(nums)
            else self.findWays(nums, pos + 1, cur + nums[pos])
            + self.findWays(nums, pos + 1, cur - nums[pos])
        )

    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        return self.findWays(tuple(nums), 0, S)


# @lc code=end
