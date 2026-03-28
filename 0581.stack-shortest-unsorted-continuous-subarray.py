#
# @lc app=leetcode id=581 lang=python3
#
# [581] Shortest Unsorted Continuous Subarray
#

# @lc code=start
from collections import deque


class Solution:
    def findUnsortedSubarray(self, nums) -> int:
        increment = deque()
        lo, hi = len(nums), 0
        for i in range(len(nums)):
            while increment and nums[increment[-1]] > nums[i]:
                lo = min(lo, increment.pop())
            increment.append(i)

        increment.clear()
        for i in reversed(range(len(nums))):
            while increment and nums[increment[-1]] < nums[i]:
                hi = max(hi, increment.pop())
            increment.append(i)

        return max(0, hi - lo + 1)


# @lc code=end
