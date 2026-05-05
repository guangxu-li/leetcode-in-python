#
# @lc app=leetcode id=221 lang=python3
#
# [221] Maximal Square
#

# @lc code=start
from typing import List


# dp[i][j] means the maximal square which bottom-right corner is at (i, j)
# dp[0][j] = matrix[0]
# dp[i][0] = matrix[i][0]
#
# If matrix[i][j] = 0, dp[i][j] = 0
# else dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
#
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 2 2
# 1 0 0 1 0
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [0] * n

        _max = 0
        prev = 0
        for i in range(m):
            for j in range(n):
                if j == 0:
                    prev, dp[j] = dp[j], int(matrix[i][j])
                elif matrix[i][j] == "0":
                    prev, dp[j] = dp[j], 0
                elif matrix[i][j] == "1":
                    prev, dp[j] = dp[j], min(dp[j], dp[j - 1], prev) + 1
                _max = max(_max, dp[j] * dp[j])

        return _max


# @lc code=end
