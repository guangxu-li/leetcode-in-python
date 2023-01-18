#
# @lc app=leetcode id=918 lang=python3
#
# [918] Maximum Sum Circular Subarray
#

# @lc code=start
from itertools import accumulate
from typing import List


# two pattern candidates:
#   1. subarray at head + subarray at tail
#   2. continuous subarray
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        prefix_sum = list(accumulate(nums)) + [0]
        right_max = [-float("inf")] * (n - 1) + [0]  # max suffix sum after i (exclusive)

        suffix_sum = nums[-1]
        for i in reversed(range(n - 1)):
            right_max[i] = max(suffix_sum, right_max[i + 1])
            suffix_sum += nums[i]

        local_max = global_max = -float("inf")
        for i, num in enumerate(nums):
            local_max = max(num, num + local_max)  # dp[i] = max(nums[i], nums[i] + dp[i - 1])
            global_max = max(global_max, local_max, prefix_sum[i] + right_max[i])

        return int(global_max)


# @lc code=end
