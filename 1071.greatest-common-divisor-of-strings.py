#
# @lc app=leetcode id=1071 lang=python3
#
# [1071] Greatest Common Divisor of Strings
#

# @lc code=start
#
# If str1 + str2 == str2 + str1, then there there must be an answer.
# And the answer is str1[gcd_len] or str2[gcd_len]
from math import gcd


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        return "" if str1 + str2 != str2 + str1 else str1[:gcd(len(str1), len(str2))]
# @lc code=end
