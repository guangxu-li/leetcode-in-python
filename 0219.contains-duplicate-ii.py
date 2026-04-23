#
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#


# @lc code=start
from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}
        for i, num in enumerate(nums):
            if num in d and i - d[num] <= k:
                return True
            d[num] = i

        return False


# @lc code=end
