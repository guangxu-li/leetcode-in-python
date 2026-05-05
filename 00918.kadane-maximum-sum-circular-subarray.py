#
# @lc app=leetcode id=918 lang=python3
#
# [918] Maximum Sum Circular Subarray
#

# @lc code=start
from typing import List


# two patterns
#   1. prefix subarray + suffix subarray -> calculated by calculated the min continuous subarray between them
#   2. max continuous subarray
#
# reverse Kadane's algorithm + Kadane's algorithm
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        local_min = global_min = float("inf")
        local_max = global_max = -float("inf")
        for num in nums:
            local_min = min(num, num + local_min)
            local_max = max(num, num + local_max)
            global_min = min(global_min, local_min)
            global_max = max(global_max, local_max)

        # edge case: all negative -> global_min = sum(nums)
        # but empty subarray is not allowed
        return int(global_max if global_max < 0 else max(global_max, sum(nums) - global_min))


# @lc code=end
