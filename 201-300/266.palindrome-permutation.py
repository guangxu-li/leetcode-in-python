#
# @lc app=leetcode id=266 lang=python3
#
# [266] Palindrome Permutation
#

# @lc code=start
from collections import Counter


class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        return sum(1 for _, cnt in Counter(s).items() if cnt % 2) == len(s) % 2


# @lc code=end
