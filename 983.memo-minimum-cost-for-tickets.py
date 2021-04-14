#
# @lc app=leetcode id=983 lang=python3
#
# [983] Minimum Cost For Tickets
#

# @lc code=start
from functools import lru_cache
from bisect import bisect_left


class Solution:
    @lru_cache(maxsize=None)
    def min_cost(self, days: tuple, pos: int, costs: tuple) -> int:
        if pos == len(days):
            return 0

        return min(
            c + self.min_cost(days, bisect_left(days, days[pos] + l), costs) for c, l in costs
        )

    def mincostTickets(self, days: list[int], costs: list[int]) -> int:
        return self.min_cost(tuple(days), 0, tuple(zip(costs, [1, 7, 30])))


# @lc code=end
