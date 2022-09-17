#
# @lc app=leetcode id=342 lang=python3
#
# [342] Power of Four
#

# @lc code=start
from math import log2

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and log2(n) % 2 == 0
# @lc code=end

