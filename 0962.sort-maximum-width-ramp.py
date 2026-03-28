#
# @lc app=leetcode id=962 lang=python3
#
# [962] Maximum Width Ramp
#

# @lc code=start

# First solve this problem:
# Given a sequences of num, find the maximum of nums[j] - nums[i], i < j

# This problem could be solved by transforming to the above problem.
# If we sorted the input nums index by it's correspoinding values.
# The when we traverse from left to the right, the coreesponding value must be increasing. And the only condition to meet is to find the largest index value gap,
# which is exactly same as the above problem.

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        idxs = sorted([i for i in range(len(nums))], key=lambda i: nums[i])
        _min = float("inf")
        width = 0
        for i in idxs:
            width = max(width, i - _min)
            _min = min(_min, i)

        return width

# @lc code=end
