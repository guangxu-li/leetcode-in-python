#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        amnt = 0
        lo, hi = 0, len(height) - 1
        lo_max = hi_max = 0

        while lo < hi:
            if height[lo] <= height[hi]:
                amnt += max(0, lo_max - height[lo])
                lo_max = max(lo_max, height[lo])
                lo += 1
            else:
                amnt += max(0, hi_max - height[hi])
                hi_max = max(hi_max, height[hi])
                hi -= 1

        return amnt


# @lc code=end
