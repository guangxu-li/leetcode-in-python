#
# @lc app=leetcode id=1413 lang=python3
#
# [1413] Minimum Value to Get Positive Step by Step Sum
#

# @lc code=start
class Solution:
    def minStartValue(self, nums: list[int]) -> int:
        _sum, _min = 0, 0
        for num in nums:
            _sum += num
            _min = min(_min, _sum)
        
        return 1 - _min
# @lc code=end

