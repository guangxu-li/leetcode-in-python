#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#

# @lc code=start
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # reset:    ready to buy
        # held:     bought and ready to sell
        # cooldown: sold and cooldown
        #
        # current stage -> possible next state
        #   reset     -> reset, held
        #   held      -> held,  cooldown
        #   cooldown  -> reset
        #
        # define dp[i][state] as max profit of prices[i:] staring with the state
        #
        # dp[i][reset]   :      max(dp[i+1][reset], dp[i+1][held]     - price[i])
        # dp[i][held]    :      max(dp[i+1][held],  dp[i+1][cooldown] + price[i])
        # dp[i][cooldown]:      dp[i+1][reset]
        #
        # scan from left to right version
        # define dp[i][state] as max profit of prices[:i+1] ending with the state
        # dp[i][reset]   :      max(dp[i-1][reset], dp[i-1][cooldown])
        # dp[i][held]    :      max(dp[i-1][held],  dp[i-1][reset] - prices[i])
        # dp[i][cooldown]:      dp[i-1][held] + prices[i]
        #
        # in this case, there's no cooldown state, and held transit to reset state immediately

        reset = held = 0
        for price in reversed(prices):
            reset, held = max(reset, held - price), max(held, reset + price)
        return reset

        # reset, held = 0, -math.inf
        # for price in prices:
        #     reset, held = max(reset, held + price), max(held, reset - price)
        # return max(reset, held)


# @lc code=end
