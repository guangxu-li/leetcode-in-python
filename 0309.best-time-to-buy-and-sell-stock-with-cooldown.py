#
# @lc app=leetcode id=309 lang=python3
#
# [309] Best Time to Buy and Sell Stock with Cooldown
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
        #   dp[i][reset]   :      max(dp[i+1][reset], dp[i+1][held]     - price[i])
        #   dp[i][held]    :      max(dp[i+1][held],  dp[i+1][cooldown] + price[i])
        #   dp[i][cooldown]:      dp[i+1][reset]
        #
        # scan from left to right version
        # define dp[i][state] as max profit of prices[:i+1] ending with the state
        #   dp[i][reset]   :      max(dp[i-1][reset], dp[i-1][cooldown])
        #   dp[i][held]    :      max(dp[i-1][held],  dp[i-1][reset] - prices[i])
        #   dp[i][cooldown]:      dp[i-1][held] + prices[i]

        reset = held = cooldown = 0
        for price in reversed(prices):
            reset, held, cooldown = max(reset, held - price), max(held, cooldown + price), reset
        return reset

        # reset, held, cooldown = 0, -math.inf, -math.inf
        # for price in prices:
        #     reset, held, cooldown = max(reset, cooldown), max(held, reset - price), held + price
        # return max(reset, held, cooldown)


# @lc code=end
