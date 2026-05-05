#
# @lc app=leetcode id=123 lang=python3
#
# [123] Best Time to Buy and Sell Stock III
#

# @lc code=start
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # state = cash, held
        #   cash: cash, held-cost
        #   held: held, cash+profit
        #
        # dp[i][state][k] is start with state before processing prices[i], max profit we can achieve in the end
        #   dp[i][cash][k] = max(dp[i+1][cash][k], dp[i+1][held][k]     - price)
        #   dp[i][held][k] = max(dp[i+1][held][k], dp[i+1][cash][k - 1] + price)

        dp = [[0] * 3 for _ in range(2)]
        for price in reversed(prices):
            for k in range(1, 3):
                dp[0][k] = max(dp[0][k], dp[1][k] - price)
                dp[1][k] = max(dp[1][k], dp[0][k - 1] + price)
        return dp[0][2]


# @lc code=end
