#
# @lc app=leetcode id=746 lang=python3
#
# [746] Min Cost Climbing Stairs
#

# @lc code=start
from typing import List


# dp[i] means the min cost when climb starting from i.
# dp[i] = cost[i] + min(dp[i + 1], dp[i + 2])
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        a, b = 0, 0
        for c in reversed(cost):
            a, b = b, min(a, b) + c

        return min(a, b)


# @lc code=end
