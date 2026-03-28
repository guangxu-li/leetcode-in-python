#
# @lc app=leetcode id=1359 lang=python3
#
# [1359] Count All Valid Pickup and Delivery Options
#

# @lc code=start
from math import factorial


class Solution:
    def countOrders(self, n: int) -> int:
        # f(x, y) = x * f(x - 1, y + 1) + y * f(x, y - 1)
        # x -> number of pickup not finished, y -> number of pickup finished

        mod = 10 ** 9 + 7
        dp = [0] * (n + 1)
        for x in range(n + 1):
            for y in range(n + 1 - x):
                if not x:
                    dp[y] = factorial(y) % mod
                elif not y:
                    prev = dp[y] = x * dp[y + 1] % mod
                else:
                    cur = dp[y]
                    dp[y] = (x * dp[y + 1] + y * prev) % mod
                    prev = cur
        
        return dp[0]


# @lc code=end
