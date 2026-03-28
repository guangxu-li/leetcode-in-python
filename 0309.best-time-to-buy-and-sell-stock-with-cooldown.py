#
# @lc app=leetcode id=309 lang=python3
#
# [309] Best Time to Buy and Sell Stock with Cooldown
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        reset, held, sold = 0, float('-inf'), float('-inf')
        for price in prices:
            prev_reset = reset
            reset = max(reset, sold)
            sold = held + price
            held = max(held, prev_reset - price)
        
        return max(reset, held, sold)
# @lc code=end

