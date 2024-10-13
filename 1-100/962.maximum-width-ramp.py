#
# @lc app=leetcode id=962 lang=python3
#
# [962] Maximum Width Ramp
#

# Build the monostack in descending order with the indexs
# Traverse from right to left, candidate answer is found when the nums[stack[-1]] <= nums[hi].
# And we can safely pop the stack. Even if the following 'hi' pass the condition, the gap won't be the largest.

# @lc code=start
class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []
        for i, num in enumerate(nums):
            if not stack or nums[stack[-1]] > num:
                stack.append(i)

        width = 0
        for i in reversed(range(len(nums))):
            while stack and nums[stack[-1]] <= nums[i]:
                width = max(width, i - stack.pop())
        return width

# @lc code=end
