#
# @lc app=leetcode id=1808 lang=python3
#
# [1808] Maximize Number of Nice Divisors
#

# @lc code=start
class Solution:
    def maxNiceDivisors(self, n: int) -> int:
        """
        maximize x^(n / x), calculate it's derivative: n*x^(n/x -2)*(1 - ln(x))
        it reaches peak point when x == e
        which means we should take 3 as much as possible, for the reminder, we take 2
        """
        mod = 10 ** 9 + 7
        if n <= 3:
            return n
        if not n % 3:
            return pow(3, n // 3, mod)
        if n % 3 == 1:
            return pow(3, n // 3 - 1, mod) * 4 % mod
        if n % 3 == 2:
            return pow(3, n // 3, mod) * 2 % mod
# @lc code=end

