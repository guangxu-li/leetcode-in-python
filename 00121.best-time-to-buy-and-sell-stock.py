#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
import math
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

        dp = [[0] * 2 for _ in range(2)]
        for price in reversed(prices):
            dp[0][1] = max(dp[0][1], dp[1][1] - price)
            dp[1][1] = max(dp[1][1], dp[0][0] + price)
        return dp[0][1]


# @lc code=end
