#
# @lc app=leetcode id=1593 lang=python3
#
# [1593] Split a String Into the Max Number of Unique Substrings
#

# @lc code=start
from typing import Set


class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        cnt = 0
        def dfs(strs: Set[str], cur: str, i: int) -> None:
            if i == len(s):
                nonlocal cnt
                cnt = max(cnt, len(strs) + (cur not in strs))
                return

            dfs(strs, cur + s[i], i + 1)
            if cur not in strs:
                strs.add(cur)
                dfs(strs, s[i], i + 1)
                strs.discard(cur)
        dfs(set([""]), "", 0)

        return cnt - 1 # remove the ""
# @lc code=end
