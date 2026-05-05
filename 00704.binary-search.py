#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#

# Constraints:
# 1 <= nums.length <= 104
# -104 < nums[i], target < 104
# All the integers in nums are unique.
# nums is sorted in ascending order.

# @lc code=start
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums)
        while lo < hi:
            m = (lo + hi) >> 1

            if nums[m] <= target:
                lo = m + 1
            else:
                hi = m

        return -1 if hi == 0 or nums[hi - 1] != target else hi - 1


# @lc code=end
