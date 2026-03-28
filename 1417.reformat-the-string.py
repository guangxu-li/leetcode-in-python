#
# @lc app=leetcode id=1417 lang=python3
#
# [1417] Reformat The String
#

# @lc code=start
from itertools import zip_longest


class Solution:
    def reformat(self, s: str) -> str:
        group1, group2 = [ch for ch in s if ch.isdigit()], [ch for ch in s if ch.isalpha()]
        
        if len(group1) < len(group2):
            group1, group2 = group2, group1
        if len(group1) - len(group2) > 1:
            return ""
        
        return "".join(["".join(pair) for pair in zip_longest(group1, group2, fillvalue="")])
# @lc code=end
