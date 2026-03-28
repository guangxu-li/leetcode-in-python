#
# @lc app=leetcode id=962 lang=python3
#
# [962] Maximum Width Ramp
#

# 1. Build the right-max array
# 2. Setup two pointers starting from the left
# 3. Find the first lo when nums[lo] <= right_max[hi], and expand hi to explore larger gap and verify if the condition still hold

# @lc code=start
from itertools import accumulate


class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        reverse = nums[::-1]
        right_max = list(accumulate(reverse, func=max))
        right_max.reverse()

        width = lo = hi = 0
        while hi < len(nums):
            while nums[lo] > right_max[hi]:
                lo += 1

            width = max(width, hi - lo)
            hi += 1

        return width

# @lc code=end
