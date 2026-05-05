#
# @lc app=leetcode id=403 lang=python3
#
# [403] Frog Jump
#

# @lc code=start
from functools import lru_cache
from typing import List


class Solution:
    def canCross(self, stones: List[int]) -> bool:
        end = stones[-1]
        stones = set(stones)

        @lru_cache(None)
        def dfs(stone: int, step: int):
            if stone not in stones or step < 1:
                return False
            if stone == end:
                return True

            for nstep in [step - 1, step, step + 1]:
                if dfs(stone + step, nstep):
                    return True

            return False

        return dfs(0, 1)
# @lc code=end
