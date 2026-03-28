#
# @lc app=leetcode id=647 lang=python3
#
# [647] Palindromic Substrings
#

# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        cnt = 0
        for i in range(2 * len(s) - 1):
            lo, hi = i // 2, (i + 1) // 2
            while lo >= 0 and hi < len(s) and s[lo] == s[hi]:
                cnt += 1
                lo -= 1
                hi += 1
        
        return cnt
# @lc code=end


