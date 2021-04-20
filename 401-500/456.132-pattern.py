#
# @lc app=leetcode id=456 lang=python3
#
# [456] 132 Pattern
#

# @lc code=start
from collections import deque
from itertools import accumulate


class Solution:
    def find132pattern(self, nums: list[int]) -> bool:
        mins, stack = list(accumulate(nums, min)), deque()
        for i in range(len(nums) - 1, -1, -1):
            while stack and stack[-1] <= mins[i]:
                stack.pop()

            if stack and nums[i] > stack[-1] > mins[i]:
                return True
            stack.append(nums[i])

        return False


# @lc code=end
