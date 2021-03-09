#
# @lc app=leetcode id=1332 lang=python3
#
# [1332] Remove Palindromic Subsequences
#

# @lc code=start
class Solution:
    def removePalindromeSub(self, s: str) -> int:
        for i in range((len(s) + 1) // 2):
            if s[i] != s[-i - 1]:
                return 2

        return min(len(s), 1)

# @lc code=end

