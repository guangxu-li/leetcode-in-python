#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#


# @lc code=start
class Solution:
    def expand_center(self, s: str, lo: int, hi: int) -> tuple[int, int]:
        while 0 <= lo and hi < len(s) and s[lo] == s[hi]:
            lo -= 1
            hi += 1

        return lo + 1, hi - 1

    def longestPalindrome(self, s: str) -> str:
        lo, hi = 0, 0
        for i in range(len(s)):
            for j in range(i, i + 2):
                lo1, hi1 = self.expand_center(s, i, j)
                if hi1 - lo1 > hi - lo:
                    lo, hi = lo1, hi1

        return s[lo : hi + 1]


# @lc code=end
