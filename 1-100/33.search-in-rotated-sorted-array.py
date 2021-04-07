#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) >> 1
            if target >= nums[0] and nums[mid] < nums[0]:
                hi = mid - 1
            elif target < nums[0] and nums[mid] >= nums[0]:
                lo = mid + 1
            elif nums[mid] <= target:
                lo = mid + 1
            else:
                hi = mid - 1
        
        return hi if nums[hi] == target else -1
# @lc code=end

