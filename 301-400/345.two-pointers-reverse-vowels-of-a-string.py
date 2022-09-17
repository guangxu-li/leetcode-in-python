#
# @lc app=leetcode id=345 lang=python3
#
# [345] Reverse Vowels of a String
#

# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {e for e in "aeiouAEIOU"}

        cs = list(s)
        lo, hi = 0, len(cs) - 1
        while lo < hi:
            if cs[lo] not in vowels:
                lo += 1
            elif cs[hi] not in vowels:
                hi -= 1
            else:
                cs[lo], cs[hi] = cs[hi], cs[lo]
                lo += 1
                hi -= 1

        return "".join(cs)
# @lc code=end

