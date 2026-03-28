#
# @lc app=leetcode id=540 lang=python3
#
# [540] Single Element in a Sorted Array
#

# @lc code=start
class Solution:
    def singleNonDuplicate(self, nums: list[int]) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) >> 1
            if nums[mid - 1] < nums[mid] < nums[mid + 1]:
                return nums[mid]

            flag = (hi - mid) % 2
            if flag:
                if nums[mid - 1] == nums[mid]:
                    lo = mid + 1
                else:
                    hi = mid - 1
            else:
                if nums[mid - 1] == nums[mid]:
                    hi = mid - 2
                else:
                    lo = mid + 2
                
        return nums[lo]
# @lc code=end


