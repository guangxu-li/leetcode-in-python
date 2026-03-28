#
# @lc app=leetcode id=1359 lang=python3
#
# [1359] Count All Valid Pickup and Delivery Options
#

# @lc code=start
from functools import reduce
import math


class Solution:
    def countOrders(self, n: int) -> int:
        mod = 10 ** 9 + 7
        # return (math.factorial(n << 1) >> n) % mod
        return reduce(lambda cnt, i: cnt * math.comb(i << 1, 2) % mod, range(1, n + 1))


# @lc code=end
