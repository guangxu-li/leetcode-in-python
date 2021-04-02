#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
from itertools import groupby


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        return [list(g) for _, g in groupby(sorted(strs, key=sorted), sorted)]
# @lc code=end

