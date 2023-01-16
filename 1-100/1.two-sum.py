#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        v2i = {}
        for i, num in enumerate(nums):
            if target - num in v2i:
                return [v2i[target - num], i]
            v2i[num] = i

        return []

# @lc code=end
