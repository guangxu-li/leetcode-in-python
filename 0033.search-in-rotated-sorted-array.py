#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1

        while lo <= hi:
            mid = (lo + hi) >> 1
            num = nums[mid]

            if num == target:
                return mid

            # left part: nums[0] <= target
            # right part: nums[-1] >= target
            if nums[0] <= target:
                if num < nums[0]:
                    hi = mid - 1
                elif num > target:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:
                if num >= nums[0]:
                    lo = mid + 1
                elif num < target:
                    lo = mid + 1
                else:
                    hi = mid - 1

        return -1
# @lc code=end
