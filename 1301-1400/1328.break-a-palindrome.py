#
# @lc app=leetcode id=1328 lang=python3
#
# [1328] Break a Palindrome
#

# @lc code=start
class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        if n == 1:
            return ""

        for i, ch in enumerate(palindrome[: n // 2]):
            if ch != "a":
                return palindrome[:i] + "a" + palindrome[i + 1 :]
        return palindrome[: n - 1] + "b"


# @lc code=end
