#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#


# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        t = "#" + "#".join(s) + "#"  # convert to odd case
        n = len(t)
        p = [0] * n  # palindrome with i as center's radius excluding the center
        lo = mid = hi = 0

        for i in range(len(t)):
            if i < mid + p[mid]:
                p[i] = min(mid + p[mid] - i, p[2 * mid - i])
            while 0 <= i - p[i] - 1 and i + p[i] + 1 < n and t[i - p[i] - 1] == t[i + p[i] + 1]:
                p[i] += 1

            if i + p[i] > mid + p[mid]:
                mid = i

            if p[i] > hi - lo:
                lo = (i - p[i]) // 2
                hi = lo + p[i]

        return s[lo:hi]


# @lc code=end
