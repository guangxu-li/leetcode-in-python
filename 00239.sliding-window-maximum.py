#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#

# @lc code=start
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        # monotonic deque:
        #   1. expiration: remove number out of the window
        #   2. monotonic: if number >= old number, no need to keep old number

        dq = deque() # (i, num)
        ans = []
        for i, num in enumerate(nums):
            while dq and dq[0] <= i - k:
                dq.popleft()

            while dq and nums[dq[-1]] <= num:
                dq.pop()

            dq.append(i)
            if i >= k - 1:
                ans.append(nums[dq[0]])

        return ans
# @lc code=end
