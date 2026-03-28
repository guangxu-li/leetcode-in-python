#
# @lc app=leetcode id=1099 lang=python3
#
# [1099] Two Sum Less Than K
#

# @lc code=start
class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        lo, hi = 0, len(nums) - 1
        _max = -1
        while lo < hi:
            sum = nums[lo] + nums[hi]
            if sum < k:
                _max = max(_max, sum)
                lo += 1
            else:
                hi -= 1
        
        return _max
                
# @lc code=end

