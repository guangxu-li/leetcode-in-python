#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#

# @lc code=start
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo = 1
        hi = max(piles)

        while lo < hi:
            i = (lo + hi) >> 1
            days = sum((p + i - 1) // i for p in piles)

            if days > h:
                lo = i + 1
            else:
                hi = i

        return lo


# @lc code=end
