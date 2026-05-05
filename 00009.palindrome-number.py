#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#


# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev, y = 0, x
        while y > 0:
            rev = rev * 10 + y % 10
            y //= 10
        return x == rev


# @lc code=end
