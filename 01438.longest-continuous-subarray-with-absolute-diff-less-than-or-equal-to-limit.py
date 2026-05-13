#
# @lc app=leetcode id=1438 lang=python3
#
# [1438] Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
#

# @lc code=start
from collections import deque


class Solution:
    def longestSubarray(self, nums: list[int], limit: int) -> int:
        # expand sliding window with track of minimums and maximums in window by monotonic deque

        mins = deque()
        maxs = deque()

        ans = 0
        lo = 0
        for hi, num in enumerate(nums):
            while mins and mins[-1] > num:
                mins.pop()
            while maxs and maxs[-1] < num:
                maxs.pop()

            mins.append(num)
            maxs.append(num)

            while maxs[0] - mins[0] > limit:
                if nums[lo] == mins[0]:
                    mins.popleft()
                if nums[lo] == maxs[0]:
                    maxs.popleft()
                lo += 1

            ans = max(ans, hi - lo + 1)

        return ans
# @lc code=end
