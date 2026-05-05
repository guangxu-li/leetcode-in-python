#
# @lc app=leetcode id=611 lang=python3
#
# [611] Valid Triangle Number
#

# @lc code=start
from bisect import bisect_left


class Solution:
    def triangleNumber(self, nums: list[int]) -> int:
        nums = [i for i in sorted(nums) if i > 0]
        return sum(
            bisect_left(nums, nums[i] + nums[j]) - j - 1
            for i in range(len(nums))
            for j in range(i + 1, len(nums))
        )


# @lc code=end
