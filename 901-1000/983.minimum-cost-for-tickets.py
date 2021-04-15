#
# @lc app=leetcode id=983 lang=python3
#
# [983] Minimum Cost For Tickets
#

# @lc code=start
from bisect import bisect_left


class Solution:
    def mincostTickets(self, days: list[int], costs: list[int]) -> int:
        dp, costs = [0] * (len(days) + 1), list(zip(costs, [1, 7, 30]))

        for i in range(len(days) - 1, -1, -1):
            dp[i] = min(c + dp[bisect_left(days, days[i] + l)] for c, l in costs)

        return dp[0]


# @lc code=end
