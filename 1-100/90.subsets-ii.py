#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#

# @lc code=start
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        return [
            list(subset)
            for subset in set(tuple(num for i, num in enumerate(sorted(nums)) if bitmask & (1 << i)) for bitmask in range(1 << len(nums)))
        ]


# @lc code=end
