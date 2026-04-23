#
# @lc app=leetcode id=442 lang=python3
#
# [442] Find All Duplicates in an Array
#

# @lc code=start
from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 0
        while i < n:
            j = nums[i] - 1
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1

        return [nums[i] for i in range(n) if nums[i] != i + 1]


# @lc code=end
