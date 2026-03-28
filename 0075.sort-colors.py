#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#

# @lc code=start
class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lo, hi, i = 0, len(nums) - 1, 0
        while i <= hi:
            if nums[i] == 0:
                nums[lo], nums[i] = nums[i], nums[lo]
                lo += 1
                i += 1
            elif nums[i] == 2:
                nums[i], nums[hi] = nums[hi], nums[i]
                hi -= 1
            else:
                i += 1
# @lc code=end
