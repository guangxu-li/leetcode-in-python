#
# @lc app=leetcode id=526 lang=python3
#
# [526] Beautiful Arrangement
#

# @lc code=start
from math import log2
from functools import lru_cache


class Solution:
    @lru_cache(maxsize=None)
    def arrangement(self, pos: int, state: int) -> int:
        if not state:
            return 1
        
        cand, cnt = state, 0
        while cand and pos:
            p = cand & -cand
            cand ^= p
            i = log2(p) + 1

            if not pos % i or not i % pos:
                cnt += self.arrangement(pos - 1, state ^ p)
        
        return cnt


    def countArrangement(self, n: int) -> int:
        return self.arrangement(n, (1 << n) - 1)
# @lc code=end

