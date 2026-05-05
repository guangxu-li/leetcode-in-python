#
# @lc app=leetcode id=901 lang=python3
#
# [901] Online Stock Span
#

# @lc code=start
from collections import deque


class StockSpanner:
    def __init__(self):
        # strictly decrement stack
        self.prices = deque([(float("inf"), 0)])

    def next(self, price: int) -> int:
        cnt = 1
        while self.prices[-1][0] <= price:
            cnt += self.prices.pop()[1]
        self.prices.append((price, cnt))

        return cnt


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
# @lc code=end
