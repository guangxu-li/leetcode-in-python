#
# @lc app=leetcode id=2280 lang=python3
#
# [2280] Minimum Lines to Represent a Line Chart
#

# Constraints:
# 1 <= stockPrices.length <= 105
# stockPrices[i].length == 2
# 1 <= dayi, pricei <= 10^9
# All dayi are distinct.

# @lc code=start
from typing import List


class Solution:
    def minimumLines(self, prices: List[List[int]]) -> int:
        prices.sort(key=lambda x: x[0])

        n = len(prices)
        # two points can form a line
        # so at most n - 1 lines are needed
        lns = n - 1

        # we can't caculate and comare slopes due to precision issue.
        for i in range(1, n - 1):
            a, b, c = prices[i - 1], prices[i], prices[i + 1]
            if (b[1] - a[1]) * (c[0] - b[0]) == (c[1] - b[1]) * (b[0] - a[0]):
                lns -= 1

        return n
# @lc code=end
