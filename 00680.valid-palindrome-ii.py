#
# @lc app=leetcode id=680 lang=python3
#
# [680] Valid Palindrome II
#


# @lc code=start
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def validate(s: str, lo: int, hi: int) -> bool:
            while lo < hi:
                if s[lo] != s[hi]:
                    return False
                lo += 1
                hi -= 1
            return True

        lo, hi = 0, len(s) - 1
        while lo < hi:
            if s[lo] != s[hi]:
                return validate(s, lo + 1, hi) or validate(s, lo, hi - 1)
            lo += 1
            hi -= 1

        return True


# @lc code=end
