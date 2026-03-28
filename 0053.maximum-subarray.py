#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        local_max = global_max = float('-inf')
        for n in nums:
            local_max = max(n, n + local_max)
            global_max = max(local_max, global_max)
        
        return global_max
# @lc code=end

