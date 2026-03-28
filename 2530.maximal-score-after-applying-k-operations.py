#
# @lc app=leetcode id=2530 lang=python3
#
# [2530] Maximal Score After Applying K Operations
#

# @lc code=start
import heapq
from math import floor


class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        nums = [-num for num in nums]
        heapq.heapify(nums)
        score = 0
        for _ in range(k):
            score -= heapq.heapreplace(nums, floor(nums[0]/3))
        return score

# @lc code=end
