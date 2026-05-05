#
# @lc app=leetcode id=343 lang=python3
#
# [343] Integer Break
#

# @lc code=start
class Solution:
    def integerBreak(self, n: int) -> int:
        """
        maximize x^(n / x), calculate it's derivative: n*x^(n/x -2)*(1 - ln(x))
        it reaches peak point when x == e
        which means we should take 3 as much as possible, for the reminder, we take 2
        """
        if n <= 3:
            return n - 1
        if not n % 3:
            return pow(3, n // 3)
        if n % 3 == 1:
            return pow(3, n // 3 - 1) * 4
        if n % 3 == 2:
            return pow(3, n // 3) * 2
# @lc code=end

