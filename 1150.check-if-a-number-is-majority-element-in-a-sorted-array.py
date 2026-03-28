#
# @lc app=leetcode id=1150 lang=python3
#
# [1150] Check If a Number Is Majority Element in a Sorted Array
#

# @lc code=start
import bisect as bs

class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        return (
            bs.bisect(nums, target) - bs.bisect_left(nums, target)
            > len(nums) // 2
        )
# @lc code=end
