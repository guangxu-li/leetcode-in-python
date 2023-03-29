#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#

# @lc code=start
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[-1] >= nums[0]:
            return nums[0]

        lo, hi = 0, len(nums)
        while lo < hi:
            mid = (lo + hi) >> 1
            val_mid = nums[mid]

            if val_mid >= nums[0]:
                val_right = nums[mid + 1]
                if val_mid < val_right:
                    lo = mid + 1
                else:
                    return val_right
            else:
                val_left = nums[mid - 1]
                if val_left < val_mid:
                    hi = mid
                else:
                    return val_mid

        return nums[lo]


# @lc code=end
