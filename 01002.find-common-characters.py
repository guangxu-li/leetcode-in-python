#
# @lc app=leetcode id=1002 lang=python3
#
# [1002] Find Common Characters
#

# @lc code=start
from collections import Counter
from functools import reduce


class Solution:
    def commonChars(self, A: list[str]) -> list[str]:
        return reduce(Counter.__and__, map(Counter, A)).elements()
# @lc code=end

