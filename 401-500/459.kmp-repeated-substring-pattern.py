#
# @lc app=leetcode id=459 lang=python3
#
# [459] Repeated Substring Pattern
#

# @lc code=start
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        dp, n, j = [0] * len(s), len(s), 0
        for i in range(1, n):
            j = dp[i - 1]
            while j > 0 and s[i] != s[j]:
                j = dp[j - 1]

            dp[i] = j + (s[i] == s[j])
        
        return dp[-1] and not n % (n - dp[-1])
# @lc code=end

