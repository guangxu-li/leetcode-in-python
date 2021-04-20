#
# @lc app=leetcode id=503 lang=python3
#
# [503] Next Greater Element II
#

# @lc code=start
from collections import deque


class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        stack, output = deque(), [-1] * len(nums)

        for i, num in enumerate(nums * 2):
            while stack and nums[stack[-1]] < num:
                output[stack.pop()] = num
            stack.append(i % len(nums))

        return output


# @lc code=end
