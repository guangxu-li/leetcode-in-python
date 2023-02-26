#
# @lc app=leetcode id=72 lang=python3
#
# [72] Edit Distance
#

# @lc code=start
#
# dp[i][j] means the edit distance between word1[:i] and word[:j]
# dp[i][j] = min(
#   1 + dp[i][j - 1]        # insert
#   1 + dp[i - 1][j]        # delete
#   0/1 + dp[i - 1][j - 1]  # replace, 0 if word1[i - 1] == word2[j - 1]
# )
#
# dp[0][j] = j
# dp[i][0] = i
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        dp = list(range(n + 1))
        for i in range(1, m + 1):
            dp[0], prev = i, dp[0]
            for j in range(1, n + 1):
                dp[j], prev = min(1 + dp[j], 1 + dp[j - 1], (word1[i - 1] != word2[j - 1]) + prev), dp[j]

        return dp[n]


# @lc code=end
