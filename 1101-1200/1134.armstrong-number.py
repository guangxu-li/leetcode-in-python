#
# @lc app=leetcode id=1134 lang=python3
#
# [1134] Armstrong Number
#

# @lc code=start
from functools import reduce
class Solution:
    def isArmstrong(self, n: int) -> bool:
        s = str(n)
        pow = len(s)
        return n == reduce(lambda sum, a: sum + int(a) ** pow, s, 0)

# @lc code=end

