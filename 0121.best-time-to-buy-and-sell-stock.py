#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sell = _max = 0
        for price in reversed(prices):
            sell = max(sell, price)
            _max = max(_max, sell - price)

        return _max

# @lc code=end
