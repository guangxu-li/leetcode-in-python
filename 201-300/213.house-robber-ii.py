#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#

# @lc code=start
from typing import List


# If we don't consider about the circular array, then it's same as 198.house-robber
# This problem is equals to max(rob(nums[1:], rob(nums[:-1])))
class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(nums: list[int]) -> int:
            prev = cur = 0
            for num in nums:
                prev, cur = cur, max(num + prev, cur)

            return cur

        return max(nums[0], helper(nums[1:]), helper(nums[:-1]))

# @lc code=end
