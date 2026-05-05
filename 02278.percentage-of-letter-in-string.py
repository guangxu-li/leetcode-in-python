#
# @lc app=leetcode id=2278 lang=python3
#
# [2278] Percentage of Letter in String

# Constraints:
# 1 <= s.length <= 100
# s consists of lowercase English letters.
# letter is a lowercase English letter.

# @lc code=start
from collections import Counter


class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        return Counter(s)[letter] * 100 // len(s)


# @lc code=end
