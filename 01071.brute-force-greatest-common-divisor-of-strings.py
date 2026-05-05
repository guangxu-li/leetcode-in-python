#
# @lc app=leetcode id=1071 lang=python3
#
# [1071] Greatest Common Divisor of Strings
#

# @lc code=start
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) > len(str2):
            return self.gcdOfStrings(str2, str1)

        def divisible(s: str, base: str) -> bool:
            m, n = len(s), len(base)
            multi = m // n
            return s == multi * base

        for i in reversed(range(1, len(str1) + 1)):
            if len(str1) % i or len(str2) % i:
                continue

            base = str1[:i]
            if divisible(str1, base) and divisible(str2, base):
                return base

        return ""


# @lc code=end
