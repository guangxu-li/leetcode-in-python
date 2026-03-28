#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        amnt = 0

        for i, h in enumerate(height):
            while stack and height[stack[-1]] <= h:
                base = height[stack.pop()]
                if not stack:
                    break

                width = i - stack[-1] - 1
                amnt += width * (min(h, height[stack[-1]]) - base)

            stack.append(i)

        return amnt
# @lc code=end
