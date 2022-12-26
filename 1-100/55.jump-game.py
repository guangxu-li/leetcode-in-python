#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        m = 0
        for i, num in enumerate(nums):
            if i > m:
                return False
            if m >= len(nums) - 1:
                return True

            m = max(m, i + num)

        return False


# @lc code=end
