#
# @lc app=leetcode id=977 lang=python3
#
# [977] Squares of a Sorted Array
#

# @lc code=start
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        lo, hi = 0, n - 1
        output = [0] * n
        for i in range(n - 1, -1, -1):
            if abs(nums[lo]) < abs(nums[hi]):
                output[i] = nums[hi] ** 2
                hi -= 1
            else:
                output[i] = nums[lo] ** 2
                lo += 1
        
        return output
# @lc code=end

