#
# @lc app=leetcode id=718 lang=python3
#
# [718] Maximum Length of Repeated Subarray
#

# @lc code=start
class Solution:
    def findLength(self, A: list[int], B: list[int]) -> int:
        m, n = len(A), len(B)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if A[i] == B[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]

        return max(max(row) for row in dp)


# @lc code=end

