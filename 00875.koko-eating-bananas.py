#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#

# @lc code=start
import math


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        lo, hi = math.ceil(sum(piles) / h), max(piles)
        while lo < hi:
            speed = (lo + hi) >> 1
            hours = sum(math.ceil(pile / speed) for pile in piles)
            if hours > h:
                lo = speed + 1
            else:
                hi = speed
        return lo


# @lc code=end
