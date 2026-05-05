#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
import math


class Solution:
    def reverse(self, x: int) -> int:
        positive = x > 0
        x = abs(x)
        rev = 0
        while x != 0:
            x, mod = divmod(x, 10)
            if rev > 2**31 // 10:
                return 0
            elif rev == 2**31 // 10 and mod > 2**31 % 10 - int(positive):
                return 0
            rev = rev * 10 + mod
        return rev if positive else -rev


# @lc code=end
