#
# @lc app=leetcode id=879 lang=python3
#
# [879] Profitable Schemes
#

# @lc code=start
from typing import List


# dp[i][n][p] means the answer for n people, p min profit and group[i:] + profit[i:]
# size: len(group) + 1, n + 1, minProfit + 1
# dp[-1][n][0] = 1
#
# dp[i][n][p] =
#   dp[i + 1][n][p] +
#   dp[i + 1][n - group[1]][max(0, p - profit[i])] if n >= group[i]
class Solution:
    def profitableSchemes(self, n: int, mp: int, group: List[int], profit: List[int]) -> int:
        MOD = 10 ** 9 + 7
        dp = [[[0] * (mp + 1) for _ in range(n + 1)] for _ in range(len(group) + 1)]

        for j in range(n + 1):
            dp[-1][j][0] = 1

        for i in reversed(range(len(group))):
            for j in range(n + 1):
                for p in range(mp + 1):
                    dp[i][j][p] = dp[i + 1][j][p]
                    dp[i][j][p] += dp[i + 1][j - group[i]][max(0, p - profit[i])] if j >= group[i] else 0
                    dp[i][j][p] %= MOD

        return dp[0][n][mp]


# @lc code=end
