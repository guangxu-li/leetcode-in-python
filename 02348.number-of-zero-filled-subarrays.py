#
# @lc app=leetcode id=2348 lang=python3
#
# [2348] Number of Zero-Filled Subarrays
#

# @lc code=start
from typing import List


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        lo = 0
        cnt = 0
        for hi, num in enumerate(nums + [1]):
            if num:
                cnt += (hi - lo) * (hi - lo + 1) // 2
                lo = hi + 1

        return cnt


# @lc code=end
