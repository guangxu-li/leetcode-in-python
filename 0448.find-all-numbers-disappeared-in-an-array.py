#
# @lc app=leetcode id=448 lang=python3
#
# [448] Find All Numbers Disappeared in an Array
#

# @lc code=start
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i, num in enumerate(nums):
            ni = abs(num) - 1
            nums[ni] = -abs(nums[ni])
        
        missing = []
        for i, num in enumerate(nums):
            if num > 0:
                missing.append(i + 1)

            nums[i] = abs(num)
        
        return missing
# @lc code=end

