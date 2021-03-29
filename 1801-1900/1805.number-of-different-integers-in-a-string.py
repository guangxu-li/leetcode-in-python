#
# @lc app=leetcode id=1805 lang=python3
#
# [1805] Number of Different Integers in a String
#

# @lc code=start
import re


class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        return len(set(map(int, re.findall("[\d]+", word))))


# @lc code=end
