#
# @lc app=leetcode id=581 lang=python3
#
# [581] Shortest Unsorted Continuous Subarray
#

# @lc code=start
from collections import deque


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        min = float('inf')
        max = float('-inf')

        lo, hi = 0, -1
        n = len(nums) 
        for i in range(n):
            if nums[i] >= max:
                max = nums[i]
            else:
                hi = i

            if nums[n - 1 - i] <= min:
                min = nums[n - 1 - i]
            else:
                lo = n - 1 -i
        
        return hi - lo + 1

# @lc code=end
