#
# @lc app=leetcode id=1180 lang=python3
#
# [1180] Count Substrings with Only One Distinct Letter
#

# @lc code=start
class Solution:
    def countLetters(self, S: str) -> int:
        lo, hi = 0, 0
        cnt = 0
        while hi <= len(S):
            if hi == len(S) or S[hi] != S[lo]:
                n = hi - lo
                cnt += (n + 1) * n // 2
                lo = hi
            hi += 1
        
        return cnt
            

Solution().countLetters("aaaba")
# @lc code=end
