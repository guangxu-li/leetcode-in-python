#
# @lc app=leetcode id=1143 lang=python3
#
# [1143] Longest Common Subsequence
#

# @lc code=start
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [0] * (n + 1)

        for i in range(m - 1, -1, -1):
            prev = 0
            for j in range(n - 1, -1, -1):
                prev, dp[j] = dp[j], 1 + prev if text1[i] == text2[j] else max(dp[j], dp[j + 1])

        return dp[0]


# @lc code=end
