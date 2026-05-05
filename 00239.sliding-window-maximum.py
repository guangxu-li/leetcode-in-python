#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        stack = deque() # descreasing stack (storing idx)

        maxs = []
        for i, num in enumerate(nums):
            # shrink the window
            if stack and stack[0] == i - k:
                stack.popleft()

            while stack and nums[stack[-1]] <= num:
                stack.pop()
            stack.append(i)

            if i>= k - 1:
                maxs.append(nums[stack[0]])

        return maxs



# @lc code=end
