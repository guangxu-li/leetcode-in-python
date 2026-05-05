#
# @lc app=leetcode id=365 lang=python3
#
# [365] Water and Jug Problem
#

# @lc code=start
import math


class Solution:
    def canMeasureWater(self, cap1: int, cap2: int, target: int) -> bool:
        """
        https://www.youtube.com/watch?v=0Oef3MHYEC0
        """
        return cap1 + cap2 >= target and not target % math.gcd(cap1, cap2)


# @lc code=end
