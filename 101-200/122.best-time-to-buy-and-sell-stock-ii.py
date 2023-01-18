#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#

# @lc code=start
from functools import reduce
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return sum(max(0, cur - prev) for prev, cur in zip(prices, prices[1:]))


# @lc code=end
