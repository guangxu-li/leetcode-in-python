#
# @lc app=leetcode id=724 lang=python3
#
# [724] Find Pivot Index
#

# @lc code=start
class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        left, right = 0, sum(nums)
        for i, num in enumerate(nums):
            right -= num
            if left == right:
                return i
            left += num
        
        return -1

# @lc code=end

