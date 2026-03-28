#
# @lc app=leetcode id=1444 lang=python3
#
# [1444] Number of Ways of Cutting a Pizza
#

# @lc code=start
from typing import List


# apples[i][j] is the number of apples in the rectangle from (i, j) to (m - 1, n - 1)
# dp[i][j][k] is the number of ways to cut the pizza into k pieces with k - 1 cuts
#   - top-left corner is (i, j)
#   - bottom-right corner is (0, 0)
#
# if apples[i][j] == 0, dp[i][j][k] = 0
# if apples[i][j] > 0 and k == 0, dp[i][j][0] = 1
# dp[i][j][k] = sum(dp[i+1:][j][k-1]) + sum(dp[i][j+1:][k-1])
class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        MOD = 10**9 + 7
        m = len(pizza)
        n = len(pizza[0])
        apples = [[0] * (n + 1) for _ in range(m + 1)]
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                apples[i][j] = apples[i][j + 1] + apples[i + 1][j] - apples[i + 1][j + 1]
                apples[i][j] += pizza[i][j] == "A"

        dp = [[[0] * k for _ in range(n)] for _ in range(m)]
        for r in reversed(range(m)):
            for c in reversed(range(n)):
                if apples[r][c] == 0:
                    continue

                dp[r][c][0] = 1
                for nk in range(1, k):
                    for nr in range(r + 1, m):
                        if apples[r][c] > apples[nr][c]:
                            dp[r][c][nk] = (dp[r][c][nk] + dp[nr][c][nk - 1]) % MOD

                    for nc in range(c + 1, n):
                        if apples[r][c] > apples[r][nc]:
                            dp[r][c][nk] = (dp[r][c][nk] + dp[r][nc][nk - 1]) % MOD

        return dp[0][0][k - 1]


# @lc code=end
