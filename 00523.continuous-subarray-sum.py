#
# @lc app=leetcode id=523 lang=python3
#
# [523] Continuous Subarray Sum
#

# @lc code=start
class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        found, _sum = dict({0: -1}), 0
        for i, num in enumerate(nums):
            _sum += num
            if k:
                _sum %= k
            if _sum in found and i - found[_sum] > 1:
                return True
            found.setdefault(_sum, i) # don't overwrite

        return False


# @lc code=end
