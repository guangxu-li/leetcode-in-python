#
# @lc app=leetcode id=442 lang=python3
#
# [442] Find All Duplicates in an Array
#

# @lc code=start
from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicates = []
        for num in nums:
            num = abs(num)
            if nums[num - 1] < 0:
                duplicates.append(num)
            else:
                nums[num - 1] = -abs(nums[num - 1])
        return duplicates


# @lc code=end
