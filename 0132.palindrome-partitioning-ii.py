#
# @lc app=leetcode id=132 lang=python3
#
# [132] Palindrome Partitioning II
#

# @lc code=start

# dp[i] means the cuts that are needed for the substring s [:i]
# We iterate each character in s. And assume it as the palindrome center.
#
# S: "aab"
# dp: 001
# dp[1] = min(dp[2], 1 + dp[-1])
class Solution:
    def minCut(self, s: str) -> int:
        dp = list(range(len(s))) + [-1]
        for i in range(len(s)):
            # odd length palindrome
            r = 0
            while i - r >= 0 and i + r < len(s) and s[i - r] == s[i + r]:
                dp[i + r] = min(dp[i + r], 1 + dp[i - r - 1])
                r += 1

            # even length palindrome
            r = 0
            while i - r >= 0 and i + 1 + r < len(s) and s[i - r] == s[i + 1 + r]:
                dp[i + 1 + r] = min(dp[i + 1 + r], 1 + dp[i - r - 1])
                r += 1

        return dp[len(s) - 1]


# @lc code=end
