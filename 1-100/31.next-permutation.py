#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#

# @lc code=start
from bisect import bisect


class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        if i < 0:
            nums.reverse()
        else:
            tail = nums[i + 1:]
            tail.reverse()

            j = bisect(tail, nums[i])
            nums[i], tail[j] = tail[j], nums[i]

            for j, num in enumerate(tail):
                nums[i + j + 1] = num
# @lc code=end

