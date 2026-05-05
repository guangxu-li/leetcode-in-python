#
# @lc app=leetcode id=188 lang=python3
#
# [188] Best Time to Buy and Sell Stock IV
#

# @lc code=start
from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # state = cash, held
        #   cash: cash, held-cost
        #   held: held, cash+profit
        #
        # dp[i][state][k] is start with state before processing prices[i], max profit we can achieve in the end
        #   dp[i][cash][k] = max(dp[i+1][cash][k], dp[i+1][held][k]     - price)
        #   dp[i][held][k] = max(dp[i+1][held][k], dp[i+1][cash][k - 1] + price)

        dp = [[0] * (k + 1) for _ in range(2)]
        for price in reversed(prices):
            for i in range(1, k + 1):
                dp[0][i] = max(dp[0][i], dp[1][i] - price)
                dp[1][i] = max(dp[1][i], dp[0][i - 1] + price)
        return dp[0][k]


# @lc code=end
